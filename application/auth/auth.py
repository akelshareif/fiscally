""" User registration and authorization logic """

from flask import Blueprint, render_template, redirect, request, flash, session, url_for
from flask_login import login_required, logout_user, current_user, login_user
from application import db, oauth, login_manager
from .auth_forms import LoginForm, RegisterForm
from ..user.user_models import User

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


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@auth_bp.route('/login', methods=['GET', 'POST'])
def login_display():
    """ Login page """

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and User.authenticate(form.email.data, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('user.user_profile'))

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
            user = User.register(form.first_name.data, form.last_name.data,
                                 form.email.data, form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('user.user_profile'))

        flash('An account already exists with inputted credentials.', 'warning')

    return render_template('auth/register.jinja', form=form)


# Google login endpoints
@auth_bp.route('/google/login')
def google_login():
    """ Show google login page """

    redirect_uri = url_for('auth.google_authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@auth_bp.route('/google/authorize')
def google_authorize():
    """ Authenticate google login and redirect to profile page """

    token = google.authorize_access_token()
    user = google.parse_id_token(token)
    # Add user data to DB
    session['user'] = user
    print(user)

    return redirect('/user')
