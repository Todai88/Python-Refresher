from flask import Blueprint

# in templates, look for templates in /home
home_blueprint = Blueprint('home', __name__, template_folder='templates')

from . import routes