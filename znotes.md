# Dev Notes

## To-Dos

-   In root templates directory, create base navbar, logged in navbar, and anon navbar templates
-   Complete home blueprint templates
-   Make user blueprint
-   Make auth blueprint which will contain all user registration and authentication views/logic
-   Make tax blueprint
-   Make api blueprint

---

## The `g` object

-   `g` is a Flask object which is used to store data and share within a single context.
-   `g` data does not persist between requests, therefore it is only populated with data and usable within a single request cycle.
-   The most common way to use the `g` object is to initialize it within a view function decorated with the `before_request` decorator. In this request, you'd initialize the `g` object to a value like an object returned from a database query: `g.user = User.query.get('user_id')`.

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

## `config.py`

-   Import `environ, path` from `os` and `load_dotenv` from `dotenv`
-   Use python-dotenv to grab environment variables from `.env`
-   Create 3 classes, a base `Config`, `ProdConfig`, and `DevConfig`. The latter two inherit from the base class.
-   The base class holds the secret key, static folder and templates folder environmental variables
-   The production and dev configs hold all the flask related env vars.

# Design Notes

-   You will need to add a favicon to the application
-   You will design a logo for the application
-   You will figure out a consistent color scheme and may actually have a global css file
