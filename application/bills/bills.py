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

    if bill_form.validate_on_submit():
        new_bill = Bill(name=bill_form.bill_name.data,
                        due_date=bill_form.bill_due_date.data, amount=bill_form.bill_amount.data, user_id=str(current_user.id))

        db.session.add(new_bill)
        db.session.commit()
        return redirect(url_for('bills.bills_display'))

    return render_template('bills/bills.jinja', bill_form=bill_form, bills=user_bills)


@bills_bp.route('/bills/delete', methods=['POST'])
@login_required
def delete_bills():
    """ Handle bill deletion """

    bill_ids = request.json['idArr']

    for id in bill_ids:
        bill = Bill.query.get_or_404(id)
        db.session.delete(bill)
        db.session.commit()

    num_bills = Bill.query.filter_by(user_id=str(current_user.id)).count()

    return {"msg": "success", "num_bills": num_bills}
