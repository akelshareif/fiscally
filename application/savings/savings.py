from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
from application import db
from .savings_forms import SavingsForm, SavingsGoalForm
from ..models import SavingsEntry, SavingsGoal, SavingsTotal
from .savings_helper import recalculate_totals


savings_bp = Blueprint('savings', __name__,
                       url_prefix='/user', template_folder='templates')


@savings_bp.route('/savings', methods=['GET', 'POST'])
@login_required
def savings_display():
    """ Add and show savings """

    savings_form = SavingsForm()
    goal_form = SavingsGoalForm()

    savings_entries_and_totals = db.session.query(
        SavingsEntry, SavingsTotal).filter(SavingsEntry.user_id == str(current_user.id)).filter(SavingsEntry.id == SavingsTotal.savings_id).all()

    if savings_form.validate_on_submit():
        new_entry = SavingsEntry(savings_date=savings_form.savings_date.data,
                                 transaction_type=savings_form.transaction_type.data, amount=savings_form.amount.data, user_id=str(current_user.id))

        db.session.add(new_entry)
        db.session.commit()

        fresh_savings_entries = SavingsEntry.query.filter_by(
            user_id=str(current_user.id)).all()

        calculated_total = sum([savings.amount if savings.transaction_type ==
                                '+' else -savings.amount for savings in fresh_savings_entries])
        new_savings_total = SavingsTotal(
            total=calculated_total, savings_id=str(new_entry.id), user_id=str(current_user.id))

        db.session.add(new_savings_total)
        db.session.commit()

        return redirect(url_for('savings.savings_display'))

    return render_template('savings/savings.jinja', savings_form=savings_form, goal_form=goal_form, savings_totals=savings_entries_and_totals)


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
        recalculate_totals(SavingsEntry, SavingsTotal, current_user, db)

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
    recalculate_totals(SavingsEntry, SavingsTotal, current_user, db)

    return {"msg": "success"}


@savings_bp.route('/savings/goal', methods=['POST'])
@login_required
def savings_goal():
    """ Handle savings goal form """

    goal_form = SavingsGoalForm()
    if goal_form.validate_on_submit():
        print(goal_form.data)

    return {"msg": "success"}
