from application import db


class GenericModel(db.Model):
    """ Generic Model Class """

    __tablename__ = 'a_table_name'

    # Columns Here
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)

    # Optional properties, class and instance methods here
