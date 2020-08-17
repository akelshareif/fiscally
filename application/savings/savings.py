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

    if savings_form.validate_on_submit():
        print(savings_form.data)

    return render_template('savings/savings.jinja', savings_form=savings_form, goal_form=goal_form)


@savings_bp.route('/savings/goal', methods=['POST'])
@login_required
def savings_goal():
    """ Handle savings goal form """

    goal_form = SavingsGoalForm()
    if goal_form.validate_on_submit():
        print(goal_form.data)

    return {"msg": "success"}
