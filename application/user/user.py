""" User views """

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
# from .user_models import User

user_bp = Blueprint('user', __name__, url_prefix='/user',
                    template_folder='templates')


@user_bp.route('/')
@login_required
def user_profile():
    """ User profile page """

    return 'User Profile'
