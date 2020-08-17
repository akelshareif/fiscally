from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from .bill_forms import BillForm

bills_bp = Blueprint('bills', __name__, url_prefix='/user',
                     template_folder='templates')


@bills_bp.route('/bills', methods=['GET', 'POST'])
@login_required
def bills_display():
    """ Show and add bills  """

    bill_form = BillForm()

    if bill_form.validate_on_submit():
        print(bill_form.data)

    return render_template('bills/bills.jinja', bill_form=bill_form)
