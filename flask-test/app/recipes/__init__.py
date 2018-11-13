from flask import Blueprint
from . import routes

recipes_blueprint = Blueprint('recipes', __name__, template_folder='templates')

