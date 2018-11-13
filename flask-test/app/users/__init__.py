from flask import Blueprint
from . import routes

users_blueprint = Blueprint('users', __name__, template_folder='templates')
