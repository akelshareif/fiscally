""" Forms related to user registration and authentication """

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Optional, Length, Regexp


class RegisterForm(FlaskForm):
    """ Registration form for new user """

    first_name = StringField('First Name', validators=[
                             InputRequired(message='First name is required.')])
    last_name = StringField('Last Name', validators=[
                            InputRequired(message='Last name is required.')])
    email = StringField('Email', validators=[InputRequired(
        message='Enter a valid email.'), Email(message='Enter a valid email.')])
    password = PasswordField('Password', validators=[
                             InputRequired(message='Password is required.'), Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*\#\?&])[A-Za-z\d@$!#%*?&]{8,40}$', message="Password must be at least 8 characters long, contain upper and lowercase characters, at least one special character, and at least one number.")])


class LoginForm(FlaskForm):
    """ Login form for returning user """

    email = StringField('Email', validators=[
                        InputRequired(message='You must enter an Email Address.'), Email(message='Enter a valid email.')])
    password = PasswordField('Password', validators=[
                             InputRequired(message='Password is required.')])


class EmailVerificationForm(FlaskForm):
    """ Form to verify email and send verification code """

    email = StringField('Email', validators=[InputRequired(
        message='You must enter an Email Address.'), Email(message='Enter a valid email.')])


class VerifyCodeForm(FlaskForm):
    """ Form to enter the verification code """

    verification_code = StringField('Verification Code', validators=[InputRequired(
        message="You must enter the verification code sent to your email.")])


class ResetPasswordForm(FlaskForm):
    """ Form to reset password """

    new_password = PasswordField('New Password', validators=[
        InputRequired(message="You must enter a new password"), Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*\#\?&])[A-Za-z\d@$!#%*?&]{8,40}$', message="Password must be at least 8 characters long, contain upper and lowercase characters, at least one special character, and at least one number.")])

    verify_password = PasswordField('Confirm New Password', validators=[
        InputRequired(message="You must verify your password"), Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*\#\?&])[A-Za-z\d@$!#%*?&]{8,40}$', message="Password must be at least 8 characters long, contain upper and lowercase characters, at least one special character, and at least one number.")])
