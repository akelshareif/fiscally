from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from application import db
from .bill_forms import BillForm
from ..models import Bill

bills_bp = Blueprint('bills', __name__, url_prefix='/user',
                     template_folder='templates')


@bills_bp.route('/bills', methods=['GET', 'POST'])
@login_required
def bills_display():
    """ Show and add bills  """

    bill_form = BillForm()

    if bill_form.validate_on_submit():
        new_bill = Bill(name=bill_form.bill_name.data,
                        due_date=bill_form.bill_due_date.data, amount=bill_form.bill_amount.data)

        db.session.add(new_bill)
        db.session.commit()
        return redirect(url_for('bills.bills_display'))

    return render_template('bills/bills.jinja', bill_form=bill_form)
