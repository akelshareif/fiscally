# Dev Notes

## Blueprints

-   In a `blueprint.py` file, you import the models and forms as usual but preprend a dot `.` to the correct file name
-   In redirects within a `blueprint.py` file or links in jinja templates, you use `url_for(directory.route_name)`
-   If you pass in the `url_prefix` keyword argument to the Blueprint object and initialize it to a url like `/random`, you can use relative paths in all endpoints of the `blueprint.py` file
-   In a blueprint's model.py file, you only import `db` from `application` or `..`
-   When making the `templates` directory, make a sub-directory of the same name as the main blueprint directory. Placing templates within this sub-directory avoids template overriding.

## `__init__.py`

-   Import `flask` and `flask_sqlalchemy` and then instantiate SQLAlchemy with the `db` variable.
-   Make a flask application factory function named `create_app` and pass in `test_config=None` as an argument.
-   Inside the factory function, instantiate the flask app and `app.config`
-   Connect the app and the database as usual
-   Within `with app.app_context():` import your blueprints and create the database tables
-   Register the blueprints and return the flask app object

## Design Notes

-   You will need to add a favicon to the application
-   You will design a logo for the application
-   You will figure out a consistent color scheme and may actually have a global css file
