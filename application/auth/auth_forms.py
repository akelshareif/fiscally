""" Forms related to user registration and authentication """

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Optional, Length


class RegisterForm(FlaskForm):
    """ Registration form for new user """

    first_name = StringField('First Name', validators=[InputRequired(
        message='First name is required.'), Length(max=20)])
    last_name = StringField('Last Name', validators=[InputRequired(
        message='Last name is required.'), Length(max=20)])
    email = StringField('Email', validators=[InputRequired(
        message='Enter a valid email.'), Email()])
    password = PasswordField('Password', validators=[
                             InputRequired(message='Password is required.')])


class LoginForm(FlaskForm):
    """ Login form for returning user """

    email = StringField('Email', validators=[
                        InputRequired(message='Enter a valid email.')])
    password = PasswordField('Password', validators=[
                             InputRequired(message='Password is required.')])
