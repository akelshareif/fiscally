from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, RadioField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired


class SavingsForm(FlaskForm):
    """ Form to add or subtract savings """

    savings_date = DateField('Transaction Date', validators=[
                             InputRequired(message="You must select a date.")])

    transaction = RadioField('Transaction Type', choices=[(
        '+', 'Deposit'), ('-', 'Withdraw')], validators=[InputRequired(message="You must select a transaction type.")])

    amount = DecimalField('Amount', validators=[
                          InputRequired(message="You must enter an amount.")])


class SavingsGoalForm(FlaskForm):
    """ Form to add a savings goal """

    goal_start = DateField('Start Date', validators=[
        InputRequired(message="You must select a date.")])

    goal_end = DateField('End Date', validators=[
        InputRequired(message="You must select a date.")])

    goal_amount = DecimalField('Savings Goal', validators=[
                               InputRequired(message="You must add a savings goal.")])
