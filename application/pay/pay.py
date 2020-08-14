""" Paycheck routes """

from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from ..models import Paycheck
from .pay_forms import WhichPayForm, WeeklyGrossForm, BiWeeklyGrossForm, BiMonthlyGrossForm, MonthlyGrossForm, PaycheckForm

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
