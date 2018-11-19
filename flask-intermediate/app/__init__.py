from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_application(config_name):
    app = Flask(__name__, instance_relative_config=True) # config from /instance
    app.config.from_pyfile(config_name)
    initialize_extensions(app)
    register_blueprints(app)

    @app.route("/")
    def index():
        return render_template("index.html", title="Index")

    @app.route("/add")
    def add():
        return render_template("add.html")

    return app


def initialize_extensions(app_instance):
    db.init_app(app_instance)

    from models import Article

def register_blueprints(app_instane):
    from home import home_blueprint

    app_instane.register_blueprint(home_blueprint)
