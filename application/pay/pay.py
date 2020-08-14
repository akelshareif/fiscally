""" Paycheck routes """

from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from ..models import Paycheck
from .pay_forms import PaycheckForm

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
    rate = float(pay_data['pay_rate'])
    weeks_hours = pay_data['hours']

    weeks_ot_hours = [
        float(hours)-40 for hours in weeks_hours if float(hours)-40 >= 0]
    weeks_ot_gross = [float(hours)*rate*1.5 for hours in weeks_ot_hours]

    weeks_base_pay = []
    for hours in weeks_hours:
        if float(hours) > 40:
            weeks_base_pay.append(40*rate)
        else:
            weeks_base_pay.append(float(hours)*rate)

    print('ot:', weeks_ot_gross)
    print('base:', weeks_base_pay)
    total_base = 0
    total_ot = 0
    for pay in weeks_base_pay:
        total_base += pay
    for pay in weeks_ot_gross:
        total_ot += pay

    total_gross = total_base+total_ot

    return {"gross": total_gross}
