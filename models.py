from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """ Connects app to database """
    db.app = app
    db.init_app(app)


class GenericModel(db.Model):
    """ Generic Model Class """

    __tablename__ = 'a_table_name'

    # Columns Here
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Optional properties, class and instance methods here
