""" Paycheck routes """

from flask import Blueprint, render_template, redirect, url_for, request, flash
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

    pay_frequency_dict = {
        "52": "Weekly",
        "26": "Bi-Weekly",
        "24": "Semi-Monthly",
        "12": "Monthly"
    }

    return render_template('pay/pay.jinja', pc_form=paycheck_form, salary_gross_form=salary_gross_form, paychecks=paychecks, pay_frequency_dict=pay_frequency_dict)


@pay_bp.route('/pay/gross/calculate', methods=['POST'])
@login_required
def calculate_gross():

    pay_data = request.json
    total_pay = calculate_gross_pay(pay_data)

    return {"gross": total_pay}


@pay_bp.route('/pay/edit/<paycheck_id>', methods=['GET'])
@login_required
def edit_paycheck(paycheck_id):
    """ Edit a paycheck """

    paycheck = Paycheck.query.get(paycheck_id)

    form = PaycheckForm(obj=paycheck)

    return render_template('pay/edit_paycheck.jinja', form=form, paycheck_id=paycheck_id)


@pay_bp.route('/pay/delete', methods=['POST'])
@login_required
def delete_paycheck():
    """ Delete a paycheck entry """

    paycheck_id = request.json['paycheckId']

    paycheck = Paycheck.query.get(paycheck_id)
    db.session.delete(paycheck)
    db.session.commit()

    return {"msg": "success"}
