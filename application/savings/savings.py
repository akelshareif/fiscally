from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from application import db
from .savings_forms import SavingsForm, SavingsGoalForm
from ..models import SavingsEntry, SavingsGoal


savings_bp = Blueprint('savings', __name__,
                       url_prefix='/user', template_folder='templates')


@savings_bp.route('/savings', methods=['GET', 'POST'])
@login_required
def savings_display():
    """ Add and show savings """

    savings_form = SavingsForm()
    goal_form = SavingsGoalForm()
    user_savings = SavingsEntry.query.filter_by(
        user_id=str(current_user.id)).all()

    total_savings = sum([savings.amount if savings.transaction_type ==
                         '+' else -savings.amount for savings in user_savings])

    if savings_form.validate_on_submit():
        new_entry = SavingsEntry(savings_date=savings_form.savings_date.data,
                                 transaction_type=savings_form.transaction_type.data, amount=savings_form.amount.data, total=total_savings, user_id=str(current_user.id))

        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for('savings.savings_display'))

    return render_template('savings/savings.jinja', savings_form=savings_form, goal_form=goal_form, savings=user_savings)


@savings_bp.route('/savings/edit/<savings_entry_id>', methods=['GET', 'POST'])
@login_required
def edit_savings_entry(savings_entry_id):
    """ Edit savings entry """

    entry = SavingsEntry.query.get(savings_entry_id)
    savings_form = SavingsEntry(obj=entry)

    return render_template('bills/edit_savings_entry.jinja', form=savings_form, entry=entry)


@savings_bp.route('/savings/delete', methods=['POST'])
@login_required
def delete_savings_entries():
    """ Delete a savings entry """

    savings_ids = request.json['idArr']

    for id in savings_ids:
        entry = SavingsEntry.query.get(id)
        db.session.delete(entry)
        db.session.commit()

    return {"msg": "success"}


@savings_bp.route('/savings/goal', methods=['POST'])
@login_required
def savings_goal():
    """ Handle savings goal form """

    goal_form = SavingsGoalForm()
    if goal_form.validate_on_submit():
        print(goal_form.data)

    return {"msg": "success"}
