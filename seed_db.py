from application import db  # Models go here
from application import app

# Create tables
db.drop_all()
db.create_all()

# Replace Model with a Model for every model to ensure all tables are empty
Model.query.delete()
