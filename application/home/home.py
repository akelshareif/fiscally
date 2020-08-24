""" Home page views """

from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

# Initialize blueprint
home_bp = Blueprint(
    'home', __name__, template_folder='templates')


# Home page endpoints
@home_bp.route('/', methods=['GET', 'POST'])
def home_page():
    """ Main root route of application """
    if current_user.is_anonymous:
        return render_template('home/landing.jinja')
    else:
        return redirect(url_for('user.user_profile'))
