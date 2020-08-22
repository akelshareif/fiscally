""" Savings routes """

from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from application import db
from .savings_forms import SavingsForm, SavingsGoalForm
from ..models import SavingsEntry, SavingsGoal, SavingsTotal
from .savings_helper import recalculate_totals, get_calculated_total, savings_progress_percentage, savings_goal_time_percentage


savings_bp = Blueprint('savings', __name__,
                       url_prefix='/user', template_folder='templates')


@savings_bp.route('/savings', methods=['GET', 'POST'])
@login_required
def savings_display():
    """ Add and show savings """

    savings_form = SavingsForm()
    goal_form = SavingsGoalForm()

    # Retrieve table data from db
    savings_entries_and_totals = db.session.query(
        SavingsEntry, SavingsTotal).filter(SavingsEntry.user_id == str(current_user.id)).filter(SavingsEntry.id == SavingsTotal.savings_id).all()

    # Handle savings_form submission
    if savings_form.validate_on_submit():
        new_entry = SavingsEntry(savings_date=savings_form.savings_date.data,
                                 transaction_type=savings_form.transaction_type.data, amount='{:.2f}'.format(savings_form.amount.data), user_id=str(current_user.id))

        db.session.add(new_entry)
        db.session.commit()

        # Get calculated total
        calculated_total = get_calculated_total(current_user)

        # Make a new SavingsTotal entry and commit to db
        new_savings_total = SavingsTotal(
            total=calculated_total, savings_id=str(new_entry.id), user_id=str(current_user.id))

        db.session.add(new_savings_total)
        db.session.commit()

        flash('Savings Entry was successfully added', 'success')
        return redirect(url_for('savings.savings_display'))

    # Retrieve savings goal data from db, calculate goal_percentage, and time elapsed percentage
    savings_goal = SavingsGoal.query.filter(
        SavingsGoal.user_id == str(current_user.id)).first()

    if savings_goal:
        goal_percentage, total_savings = savings_progress_percentage(
            savings_goal, current_user)

        days_elapsed_percentage, days_elapsed, total_goal_days = savings_goal_time_percentage(
            savings_goal)

        return render_template('savings/savings.jinja', savings_form=savings_form, goal_form=goal_form, savings_totals=savings_entries_and_totals, savings_goal=savings_goal,
                               goal_percentage=goal_percentage, total=total_savings, days_elapsed_percentage=days_elapsed_percentage, days_elapsed=days_elapsed, total_goal_days=total_goal_days)
    else:
        return render_template('savings/savings.jinja', savings_form=savings_form, goal_form=goal_form, savings_totals=savings_entries_and_totals, savings_goal=savings_goal)


@savings_bp.route('/savings/edit/<savings_entry_id>', methods=['GET', 'POST'])
@login_required
def edit_savings_entry(savings_entry_id):
    """ Edit savings entry """

    entry = SavingsEntry.query.get(savings_entry_id)
    savings_form = SavingsForm(obj=entry)

    if savings_form.validate_on_submit():
        entry.savings_date = savings_form.savings_date.data
        entry.transaction_type = savings_form.transaction_type.data
        entry.amount = savings_form.amount.data
        db.session.commit()

        # Recalculate savings_totals after edit and update db
        recalculate_totals(current_user)

        flash('Savings Entry was successfully edited', 'info')
        return redirect(url_for('savings.savings_display'))

    return render_template('savings/edit_savings_entry.jinja', form=savings_form, entry=entry)


@savings_bp.route('/savings/delete', methods=['POST'])
@login_required
def delete_savings_entries():
    """ Delete a savings entry """

    savings_ids = request.json['idArr']

    # Find and delete savings entry
    for savings_id in savings_ids:
        savings_entry = SavingsEntry.query.get(savings_id)
        db.session.delete(savings_entry)
        db.session.commit()

    # Recalculate all savings_totals after savings_entry deletion and update db
    recalculate_totals(current_user)

    flash('Savings entry successfully deleted', 'warning')
    return {"msg": "success"}


@savings_bp.route('/savings/goal', methods=['POST'])
@login_required
def savings_goal():
    """ Handle savings goal form """

    goal_form = SavingsGoalForm()

    if goal_form.validate_on_submit():
        current_goal = SavingsGoal.query.filter(
            SavingsGoal.user_id == str(current_user.id)).one_or_none()

        if current_goal:
            db.session.delete(current_goal)
            db.session.commit()

        new_goal = SavingsGoal(start_date=goal_form.goal_start.data, end_date=goal_form.goal_end.data,
                               amount=goal_form.goal_amount.data, user_id=str(current_user.id))

        db.session.add(new_goal)
        db.session.commit()

    flash('Savings goal was successfully added', 'success')
    return redirect(url_for('savings.savings_display'))


@savings_bp.route('/savings/goal/delete', methods=['POST'])
@login_required
def delete_savings_goal():
    """ Handle savings goal deletion """

    current_goal = SavingsGoal.query.filter(
        SavingsGoal.user_id == str(current_user.id)).one_or_none()

    db.session.delete(current_goal)
    db.session.commit()

    flash('Savings goal was successfully deleted', 'warning')
    return redirect(url_for('savings.savings_display'))
