""" All pay related forms """

from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, RadioField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, Optional
from .state_dict import states


class PaycheckForm(FlaskForm):
    """ Add/edit paycheck form """

    pay_method = RadioField('Pay Method', choices=[('ppp', 'Per Pay-Period'), ('a', 'Annual')], validators=[
                            InputRequired(message="You must select a salary pay method.")])

    pay_date = DateField('Pay Date', format='%Y-%m-%d',
                         validators=[InputRequired()])

    gross_pay = DecimalField('Gross Pay', places=2, validators=[
                             InputRequired(message="You must enter your gross pay.")])

    filing_status = RadioField('Filing Status', choices=[('s', 'Single'), ('m', 'Married'), ('ms', 'Married Filing Separately'), (
        'h', 'Head of Household')], validators=[InputRequired(message="You must select your filing status.")])

    state = SelectField('State', choices=list(states.items()), validators=[InputRequired(
        message="You must select the state which you've worked in.")])

    exemptions = IntegerField('Number of Exemptions', validators=[Optional()])


class SalaryGrossPayForm(FlaskForm):
    """ Form to calculate gross salary """

    salary = DecimalField('Annual Salary', places=2, validators=[
                          InputRequired(message="You must enter your annual salary.")])
    pay_frequency = RadioField('Pay Frequency', choices=[(52, 'Weekly'), (26, 'Bi-Weekly'), (24, 'Semi-Monthly'), (
        12, 'Monthly')], validators=[InputRequired(message="You must select a pay frequency.")])
