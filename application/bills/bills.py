""" Bills routes """

from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user
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

    user_bills = Bill.query.filter_by(user_id=str(current_user.id)).all()

    total_amount_due = round(
        sum([bill.bill_amount for bill in user_bills if bill.is_paid == 'Not Paid']), 2)

    if bill_form.validate_on_submit():
        new_bill = Bill(bill_name=bill_form.bill_name.data,
                        bill_due_date=bill_form.bill_due_date.data, bill_amount=bill_form.bill_amount.data, user_id=str(current_user.id))

        db.session.add(new_bill)
        db.session.commit()
        return redirect(url_for('bills.bills_display'))

    return render_template('bills/bills.jinja', bill_form=bill_form, bills=user_bills, total_amount_due=total_amount_due)


@bills_bp.route('/bills/paid', methods=['POST'])
@login_required
def mark_bill_paid():
    """ Marks a bill as paid """

    bill_ids = request.json['idArr']

    for id in bill_ids:
        bill = Bill.query.get(id)

        if bill.is_paid == 'Not Paid':
            bill.is_paid = 'Paid'
        else:
            bill.is_paid = 'Not Paid'

        db.session.commit()

    return {"msg": "success"}


@bills_bp.route('/bills/edit/<bill_id>', methods=['GET', 'POST'])
@login_required
def edit_bill(bill_id):
    """ Handle bill edit """

    bill = Bill.query.get(bill_id)

    bill_form = BillForm(obj=bill)

    if bill_form.validate_on_submit():
        bill.bill_name = bill_form.bill_name.data
        bill.bill_due_date = bill_form.bill_due_date.data
        bill.bill_amount = bill_form.bill_amount.data
        db.session.commit()
        return redirect(url_for('bills.bills_display'))

    return render_template('bills/edit_bill.jinja', form=bill_form, bill=bill)


@bills_bp.route('/bills/delete', methods=['POST'])
@login_required
def delete_bills():
    """ Handle bill deletion """

    bill_ids = request.json['idArr']

    for id in bill_ids:
        bill = Bill.query.get(id)
        db.session.delete(bill)
        db.session.commit()

    return {"msg": "success"}
