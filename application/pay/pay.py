""" Paycheck routes """

from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from application import db
from .pay_forms import PaycheckForm, SalaryGrossPayForm
from .pay_helpers import calculate_gross_pay
from ..models import Paycheck

pay_bp = Blueprint('pay', __name__, url_prefix='/user',
                   template_folder='templates')


@pay_bp.route('/pay', methods=['GET', 'POST'])
@login_required
def pay_display():
    """ Displays paycheck history and add/delete functionality """

    paycheck_form = PaycheckForm()
    salary_gross_form = SalaryGrossPayForm()

    paychecks = Paycheck.query.filter(
        Paycheck.user_id == str(current_user.id)).all()

    return render_template('pay/pay.jinja', pc_form=paycheck_form, salary_gross_form=salary_gross_form, paychecks=paychecks)


@pay_bp.route('/pay/gross/calculate', methods=['POST'])
@login_required
def calculate_gross():

    pay_data = request.json
    total_pay = calculate_gross_pay(pay_data)

    return {"gross": total_pay}


@pay_bp.route('/pay/delete/<paycheck_id>', methods=['POST'])
@login_required
def delete_paycheck(paycheck_id):
    """ Delete a paycheck entry """

    paycheck = Paycheck.query.get(paycheck_id)
    print(paycheck_id)

    return redirect(url_for('pay.pay_display'))
