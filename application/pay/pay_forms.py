""" All pay related forms """

from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, IntegerField, RadioField, SelectField, FieldList
from wtforms.fields.html5 import DateField
from wtforms.validators import InputRequired, Optional
from .state_dict import states


class WhichPayForm(FlaskForm):
    """ Used to determine appropriate pay form """

    pay_frequency = RadioField('Pay Frequency', choices=[('w', 'Weekly'), ('bw', 'Bi-Weekly'), (
        'bm', 'Bi-Monthly'), ('m', 'Monthly')], validators=[InputRequired(message="You must select a pay-frequency.")])


class WeeklyGrossForm(FlaskForm):
    """ Weekly pay data """

    pay_rate = DecimalField('Pay Rate', places=2, validators=[
                            InputRequired(message="You must enter a pay-rate.")])

    weekly_hours = DecimalField('Week Hours', places=2, validators=[
                                InputRequired(message="You must enter the hours you've worked per-week.")])


class BiWeeklyGrossForm(FlaskForm):
    """ Bi-Weekly pay data """

    pay_rate = DecimalField('Pay Rate', places=2, validators=[
                            InputRequired(message="You must enter a pay-rate.")])

    week_1_hours = DecimalField('Week One Hours', places=2, validators=[
                                InputRequired(message="You must enter the hours you've worked in week one.")])

    week_2_hours = DecimalField('Week Two Hours', places=2, validators=[
                                InputRequired(message="You must enter the hours you've worked in week two.")])


class BiMonthlyGrossForm(FlaskForm):
    """ Bi-monthly pay data """

    pay_rate = DecimalField('Pay Rate', places=2, validators=[
                            InputRequired(message="You must enter a pay-rate.")])

    week_1_hours = DecimalField('Week One Hours', places=2, validators=[
                                InputRequired(message="You must enter the hours you've worked in week one.")])

    week_2_hours = DecimalField('Week Two Hours', places=2, validators=[
                                InputRequired(message="You must enter the hours you've worked in week two.")])

    week_3_hours = DecimalField('Week Three Hours', places=2, validators=[
                                InputRequired(message="You must enter the hours you've worked in week three.")])


class MonthlyGrossForm(FlaskForm):
    """ Bi-monthly pay data """

    pay_rate = DecimalField('Pay Rate', places=2, validators=[
                            InputRequired(message="You must enter a pay-rate.")])

    week_1_hours = DecimalField('Week One Hours', places=2, validators=[
                                InputRequired(message="You must enter the hours you've worked in week one.")])

    week_2_hours = DecimalField('Week Two Hours', places=2, validators=[
                                InputRequired(message="You must enter the hours you've worked in week two.")])

    week_3_hours = DecimalField('Week Three Hours', places=2, validators=[
                                InputRequired(message="You must enter the hours you've worked in week three.")])

    week_4_hours = DecimalField('Week Four Hours', places=2, validators=[
                                InputRequired(message="You must enter the hours you've worked in week Four.")])


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
