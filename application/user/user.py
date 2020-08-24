""" User views """

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user, logout_user
from sqlalchemy import desc, exc
from application import db
from .user_forms import EditAccountForm
from ..models import Paycheck, Bill, SavingsEntry, SavingsTotal, User
from ..savings import savings_helper
from ..email_handler import send_email

user_bp = Blueprint('user', __name__, url_prefix='/user',
                    template_folder='templates')


@user_bp.route('/')
@login_required
def user_profile():
    """ User profile page """

    # Get total amount bills due
    user_bills = Bill.query.filter_by(user_id=str(current_user.id)).all()

    total_amount_due = sum(
        [bill.bill_amount for bill in user_bills if bill.is_paid == 'Not Paid'])

    # Get total savings amount
    total_savings = savings_helper.get_calculated_total(current_user)

    # Get last paycheck
    last_added_paycheck = Paycheck.query.filter_by(user_id=str(
        current_user.id)).order_by(desc(Paycheck.created)).first()

    pay_frequency_dict = {
        "52": "Weekly",
        "26": "Bi-Weekly",
        "24": "Semi-Monthly",
        "12": "Monthly"
    }

    return render_template('user/profile.jinja', amount_due=total_amount_due, savings=total_savings, paycheck=last_added_paycheck, pay_frequency_dict=pay_frequency_dict, user=current_user)


@user_bp.route('/settings')
@login_required
def account_settings():
    """ User account settings page """

    return render_template('user/account_settings.jinja')


@user_bp.route('/settings/edit', methods=['GET', 'POST'])
@login_required
def edit_account():
    """ Form to edit account settings """

    user = User.query.get(current_user.id)
    form = EditAccountForm(obj=user)

    if form.validate_on_submit():
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.email = form.email.data

        try:
            db.session.commit()

        except exc.IntegrityError:
            flash('An account with that email already exists', 'danger')
            return redirect(url_for('user.edit_account'))

        send_email(user.email, 'Fiscally: Account Updated',
                   render_template('user/account_updated_email.jinja', user=current_user))

        flash('Account settings have been successfully updated', 'success')
        return redirect(url_for('user.account_settings'))

    return render_template('user/edit_account.jinja', form=form)


@user_bp.route('/delete', methods=['POST'])
@login_required
def delete_account():
    """ Handles account deletion """

    user = User.query.get(current_user.id)
    logout_user()

    db.session.delete(user)
    db.session.commit()

    flash('You have successfully deleted your account', 'success')
    return redirect(url_for('home.home_page'))
