""" Taxee api routes """

import requests
from os import environ
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from application import db
from ..models import Paycheck
from ..pay.pay_forms import PaycheckForm


taxee_bp = Blueprint('taxee', __name__, url_prefix='/api')


@taxee_bp.route('/', methods=['POST'])
@login_required
def taxee_api():

    form = PaycheckForm()

    if form.validate_on_submit():
        # Preparing request headers and request post data
        headers = {
            'Authorization': environ.get('TAXEE_API_SECRET'),
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = {
            'pay_rate': form.gross_pay.data,
            'filing_status': form.filing_status.data,
            'state': form.state.data,
            'pay_periods': form.pay_frequency.data,
            'exemptions': form.exemptions.data
        }

        response = requests.post(
            'https://taxee.io/api/v2/calculate/2020', headers=headers, data=data)

        tax_data = response.json()['per_pay_period']

        federal_taxes = tax_data['federal']['amount']
        state_taxes = tax_data['state']['amount']
        fica_taxes = tax_data['fica']['amount']

        total_taxes = round(federal_taxes+state_taxes+fica_taxes, 2)

        net_pay = round(
            ((float(form.gross_pay.data)-float(form.pre_tax_deductions.data or 0)) - float(total_taxes)), 2)

        pay_frequency_dict = {
            "52": "Weekly",
            "26": "Bi-Weekly",
            "24": "Semi-Monthly",
            "12": "Monthly"
        }

        new_paycheck = Paycheck(pay_date=form.pay_date.data, pay_frequency=pay_frequency_dict[form.pay_frequency.data], filing_status=form.filing_status.data.capitalize(), state=form.state.data, exemptions=form.exemptions.data,
                                gross=form.gross_pay.data, pre_tax_deductions=form.pre_tax_deductions.data, federal_taxes=round(federal_taxes, 2), state_taxes=round(state_taxes, 2), fica_taxes=round(fica_taxes, 2), total_deductions=total_taxes, net=net_pay, user_id=str(current_user.id))

        db.session.add(new_paycheck)
        db.session.commit()

    return redirect(url_for('pay.pay_display'))
