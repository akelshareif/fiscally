""" User views """

from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy import desc
from ..models import Paycheck, Bill, SavingsEntry, SavingsTotal
from ..savings import savings_helper
from datetime import datetime

user_bp = Blueprint('user', __name__, url_prefix='/user',
                    template_folder='templates')


@user_bp.route('/')
@login_required
def user_profile():
    """ User profile page """

    # Get total amount bills due
    user_bills = Bill.query.filter_by(user_id=str(current_user.id)).all()
    total_amount_due = round(
        sum([bill.bill_amount for bill in user_bills if bill.is_paid == 'Not Paid']), 2)

    # Get total savings amount
    total_savings = savings_helper.get_calculated_total(current_user)

    # Get last paycheck
    last_added_paycheck = Paycheck.query.filter_by(user_id=str(
        current_user.id)).order_by(desc(Paycheck.created)).first()

    pay_frequency_dict = {
        "52": "Weekly",
        "26": "Bi-Weekly",
        "24": "Semi-Monthly",
        "12": "Monthly"
    }

    return render_template('user/profile.jinja', amount_due=total_amount_due, savings=total_savings, paycheck=last_added_paycheck, pay_frequency_dict=pay_frequency_dict, user=current_user)
