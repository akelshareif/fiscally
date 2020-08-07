from unittest import TestCase
from app import app
from models import db  # Add Models Here

# Use test DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///test_db_name'
app.config['SQLALCHEMY_ECHO'] = False

# Force flask-python errors
app.config['TESTING'] = True

db.drop_all()
db.create_all()


class GenericTestCase(TestCase):
    """ Tests view fxns """

    def setUp(self):
        """ Add sample data """

        # Disable WTForm CSRF validation
        app.config['WTF_CSRF_ENABLED'] = False

    def tearDown(self):
        """ Tests cleanup """

        db.session.rollback()
