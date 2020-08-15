""" Paycheck routes """

from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from ..models import Paycheck
from .pay_forms import PaycheckForm
from .pay_helpers import calculate_gross_pay

pay_bp = Blueprint('pay', __name__, url_prefix='/user',
                   template_folder='templates')


@pay_bp.route('/pay', methods=['GET', 'POST'])
@login_required
def pay_display():
    """ Displays paycheck history and add/delete functionality """

    paycheck_form = PaycheckForm()

    if paycheck_form.validate_on_submit():
        print(paycheck_form.pay_date.data.strftime("%m/%d/%Y"))
        # You need to access the api here to calculate the net amount
        # Then you can add data to db

    return render_template('pay/pay.jinja', pc_form=paycheck_form)


@pay_bp.route('/pay/gross/calculate', methods=['POST'])
@login_required
def calculate_gross():

    pay_data = request.json
    total_pay = calculate_gross_pay(pay_data)

    return {"gross": total_pay}
