""" Home page views """

from flask import Blueprint, render_template, request, redirect


# Initialize blueprint
home_bp = Blueprint('home', __name__, template_folder='templates')


# Home page endpoints
@home_bp.route('/', methods=['GET', 'POST'])
def home_page():
    """ Main root route of application """

    return render_template('home/home.jinja')
