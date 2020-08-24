from application import db
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from uuid import uuid4
from datetime import date, datetime, timezone


class User(UserMixin, db.Model):
    """ User Model """

    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    created = db.Column(db.TIMESTAMP, default=datetime.now())
    reset_token = db.Column(db.Text)
    paychecks = db.relationship(
        'Paycheck', backref='user', cascade='all, delete, delete-orphan')

    bills = db.relationship('Bill', backref='user',
                            cascade='all, delete, delete-orphan')

    savings_entries = db.relationship(
        'SavingsEntry', backref='user', cascade='all, delete, delete-orphan')

    savings_goals = db.relationship(
        'SavingsGoal', backref='user', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return f'<User name={self.full_name} email={self.email}>'

    @property
    def full_name(self):
        """ Returns a user's full name """
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'

    @classmethod
    def hasher(cls, hash_this):
        """ Hashes password with bcrypt """

        bcrypt = Bcrypt()

        hashed = bcrypt.generate_password_hash(hash_this)
        hashed_utf8 = hashed.decode('utf8')

        return hashed_utf8

    @classmethod
    def register(cls, first_name, last_name, email, password):
        """ Returns a User with a hashed password """

        hashed_pw = cls.hasher(password)

        return cls(first_name=first_name, last_name=last_name, email=email, password=hashed_pw)

    @classmethod
    def authenticate(cls, email, password):
        """ Returns True if user exists and password matches hash, else False """
        bcrypt = Bcrypt()

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return True
        else:
            return False


class Paycheck(db.Model):
    """ Paycheck Model """

    __tablename__ = 'paychecks'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    pay_date = db.Column(db.Date, default=date.today())
    pay_frequency = db.Column(db.Text, nullable=False)
    filing_status = db.Column(db.Text, nullable=False)
    state = db.Column(db.Text, nullable=False)
    exemptions = db.Column(db.Integer, nullable=False)
    gross_pay = db.Column(db.Float(precision=2), nullable=False)
    pre_tax_deductions = db.Column(db.Float(precision=2), default=0.00)
    federal_taxes = db.Column(db.Float(precision=2), nullable=False)
    state_taxes = db.Column(db.Float(precision=2), nullable=False)
    fica_taxes = db.Column(db.Float(precision=2), nullable=False)
    total_deductions = db.Column(db.Float(precision=2), nullable=False)
    net = db.Column(db.Float(precision=2), nullable=False)
    created = db.Column(db.TIMESTAMP, default=datetime.now())
    user_id = db.Column(UUID, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Paycheck date={self.pay_date} gross={self.gross_pay}>'


class Bill(db.Model):
    """ Bill Model """

    __tablename__ = 'bills'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    bill_name = db.Column(db.String, nullable=False)
    bill_due_date = db.Column(db.Date, default=date.today())
    bill_amount = db.Column(db.Float(precision=2), nullable=False)
    is_paid = db.Column(db.Text, default='Not Paid')
    created = db.Column(db.TIMESTAMP, default=datetime.now())
    user_id = db.Column(UUID, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Bill name={self.bill_name} amount={self.bill_amount} user={self.user_id}>'


class SavingsEntry(db.Model):
    """ Model for Savings Entries """

    __tablename__ = 'savings_entries'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    savings_date = db.Column(db.Date, default=date.today(), nullable=False)
    transaction_type = db.Column(db.String, nullable=False)
    amount = db.Column(db.Float(precision=2))
    created = db.Column(db.TIMESTAMP, default=datetime.now())
    user_id = db.Column(UUID, db.ForeignKey('users.id'))
    total_savings = db.relationship(
        'SavingsTotal', backref='savings_entries', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return f'<SavingsEntry transaction={self.transaction_type} amount={self.amount} user={self.user_id}>'


class SavingsTotal(db.Model):
    """ Total savings model """

    __tablename__ = 'total_savings_log'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    total = db.Column(db.Float(precision=2), nullable=False)
    created = db.Column(db.TIMESTAMP, default=datetime.now())
    savings_id = db.Column(UUID, db.ForeignKey('savings_entries.id'))
    user_id = db.Column(UUID, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<SavingsTotal total={self.total} savings_id={self.savings_id}>'


class SavingsGoal(db.Model):
    """ Savings Goal Model """

    __tablename__ = 'savings_goals'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    start_date = db.Column(db.Date, default=date.today(), nullable=False)
    end_date = db.Column(db.Date, default=date.today(), nullable=False)
    amount = db.Column(db.Float(precision=2), nullable=False)
    created = db.Column(db.TIMESTAMP, default=datetime.now())
    user_id = db.Column(UUID, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<SavingsGoal amount={self.amount} user={self.user_id}>'
