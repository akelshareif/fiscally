from models import db  # Models go here
from app import app

# Create tables
db.drop_all()
db.create_all()

# Replace Model with a Model for every model to ensure all tables are empty
Model.query.delete()
