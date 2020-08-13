from application import db
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from datetime import date


class User(UserMixin, db.Model):
    """ User Model """

    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    paychecks = db.relationship(
        'PaycheckModel', backref='user', cascade='all, delete, delete-orphan')

    def __repr__(self):
        return f'<User username={self.username} name={self.full_name} email={self.email}>'

    @property
    def full_name(self):
        """ Returns a user's full name """
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def register(cls, first_name, last_name, email, password):
        """ Returns a User with a hashed password """
        bcrypt = Bcrypt()

        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode('utf8')

        return cls(first_name=first_name, last_name=last_name, email=email, password=hashed_utf8)

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
    pay_date = db.Column(db.Date, nullable=False, default=date.today())
    gross = db.Column(db.Float(precision=2), nullable=False)
    net = db.Column(db.Float(precision=2), nullable=False)
    user_email = db.Column(UUID, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Paycheck user={self.user} date={self.pay_date} >'
