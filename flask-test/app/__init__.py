from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

"""
Configuration and global variables
"""
db = SQLAlchemy()
bcrypt = Bcrypt()
login = LoginManager()
login.login_view = "user.login"

"""
Factory function
"""


def create_application(cfg_fn=None):
    """
    :param cfg_fn: the name of the config file
    :return: an initialised application with extension methods added
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(cfg_fn)
    init_extensions(app)
    register_blueprints(app)
    return app


"""
Helper functions
"""


def init_extensions(app):
    """
    :param app:
    :return:
    """
    # Initialize the flask extension methods with the
    # newly set up application
    db.init_app(app)
    bcrypt.init_app(app)
    login.init_app(app)

    # Config Flask-Login
    from project.models import User

    @login.user_loader
    def load_user(user_id):
        # If multiple instances of the id, take the first
        return User.query.filter(User.id == int(user_id)).first()


def register_blueprints(app):
    """
    :param app:
    :return: void
    """
    from project.recipes import recipes_blueprints
    from project.users import users_blueprints

    app.register_blueprint(recipes_blueprints)
    app.register_blueprint(users_blueprints)
