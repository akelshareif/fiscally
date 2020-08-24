""" User registration and authorization logic """

from flask import Blueprint, render_template, redirect, request, flash, session, url_for
from flask_login import login_required, logout_user, current_user, login_user
from application import db, oauth, login_manager
from .auth_forms import LoginForm, RegisterForm, EmailVerificationForm, VerifyCodeForm, ResetPasswordForm
from ..models import User
from ..email_handler import send_email


# Create Blueprint
auth_bp = Blueprint('auth', __name__, url_prefix='/auth',
                    template_folder='templates')


# Register Google OAuth
CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
google = oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)


# Login and singup routes
@auth_bp.route('/login', methods=['GET', 'POST'])
def login_display():
    """ Login page """

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and User.authenticate(form.email.data, form.password.data):
            login_user(user)

            return redirect(url_for('user.user_profile'))

        flash('Invalid username and/or password.', 'danger')
        return redirect(url_for('auth.login_display'))

    return render_template('auth/login.jinja', form=form)


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup_display():
    """ Signup page """

    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            user = User.register(form.first_name.data.capitalize(), form.last_name.data.capitalize(),
                                 form.email.data, form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)

            send_email(user.email, 'Welcome to Fiscally!',
                       render_template('welcome_email.jinja', user=user))

            return redirect(url_for('user.user_profile'))

        flash('An account already exists with inputted credentials.', 'warning')

    return render_template('auth/register.jinja', form=form)


############## Forgot password routes ###############
@auth_bp.route('/login/forgot/verify', methods=['GET', 'POST'])
def verify_email():
    """ Email verification page """

    form = EmailVerificationForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            code = User.hasher(user.email)
            user.reset_token = code
            db.session.commit()

            session['email'] = user.email
            session.modified = True

            send_email(user.email, 'Fiscally: Email Verification Code',
                       render_template('auth/verify_email.jinja', user=user, code=code))

            flash('Verification code was successfully sent', 'success')
            return redirect(url_for('auth.verify_email_code'))
        else:
            flash('Verification code was successfully sent', 'success')
            return redirect(url_for('auth.verify_email'))

    return render_template('auth/email_verification_form.jinja', form=form)


@auth_bp.route('/login/forgot/verify/code', methods=['GET', 'POST'])
def verify_email_code():
    """ Verification code verify page """

    if session.get('email'):
        form = VerifyCodeForm()

        if form.validate_on_submit():
            user = User.query.filter_by(email=session.get('email')).first()

            if user and user.reset_token == form.verification_code.data:
                session['fiscally_data'] = user.reset_token
                session.modified = True

                flash('Verification code is successfully verified', 'success')
                return redirect(url_for('auth.reset_password'))

            else:
                session.pop('email', None)
                session.modified = True

                flash(
                    'Invalid verification code. Please re-verify your email for a new verification code.', 'danger')
                return redirect(url_for('auth.verify_email'))

        return render_template('auth/verify_code.jinja', form=form)

    else:
        flash(
            'You must first verify your email in order to reset your password', 'warning')
        return redirect(url_for('auth.verify_email'))


@auth_bp.route('/login/forgot/reset', methods=['GET', 'POST'])
def reset_password():
    """ Reset Password Page """

    if session.get('email') and session.get('fiscally_data'):
        form = ResetPasswordForm()

        if form.validate_on_submit():
            user = User.query.filter_by(email=session.get('email')).first()

            if form.new_password.data == form.verify_password.data:
                session.pop('email', None)
                session.pop('fiscally_data', None)
                new_hashed_password = User.hasher(form.new_password.data)
                user.password = new_hashed_password

                db.session.commit()
                login_user(user)

                send_email(user.email, 'Fiscally: Password Successfully Reset',
                           render_template('auth/success_pw_reset.jinja', user=user))

                flash(
                    'Password was successfully reset and you are now logged in', 'success')
                return redirect(url_for('user.user_profile'))
            else:
                flash('Passwords do not match. Please try again.', 'warning')
                return redirect(url_for('auth.reset_password'))

        return render_template('auth/reset_password.jinja', form=form)

    else:
        flash('You must first verify your email and enter a verification code in order to reset your password', 'danger')
        return redirect(url_for('auth.verify_email'))


############## Google login routes ##################
@auth_bp.route('/google/login')
def google_login():
    """ Show google login page """

    redirect_uri = url_for('auth.google_authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@auth_bp.route('/google/authorize')
def google_authorize():
    """ Handle user creation and login with google account """

    token = google.authorize_access_token()
    g_data = google.parse_id_token(token)

    # If user doesn't exists, create, login user and reirect to profile, else login user and redirect.
    user = User.query.filter_by(email=g_data['email']).first()
    if user is None:
        user = User.register(
            g_data['given_name'], g_data['family_name'], g_data['email'], g_data['sub'])
        db.session.add(user)
        db.session.commit()
        login_user(user)

        send_email(user.email, 'Welcome to Fiscally!',
                   render_template('welcome_email.jinja', user=user))

        return redirect(url_for('user.user_profile'))

    login_user(user)
    return redirect(url_for('user.user_profile'))


# Logout route
@auth_bp.route('/logout')
@login_required
def logout():
    """ Logout logic """

    logout_user()
    flash('You have successfully logged out', 'success')
    return redirect(url_for('home.home_page'))


# Flask-login authorization handlers
@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """ Redirect unauthorized users to the login page """
    flash('You must be logged in to view that page.', 'warning')
    return redirect(url_for('auth.login_display'))
