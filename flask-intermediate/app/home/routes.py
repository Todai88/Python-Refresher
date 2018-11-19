from . import home_blueprint
import json
from flask import Response, jsonify, render_template
from app.models import Article
# from app import db

@home_blueprint.route('/')
def index():
    return render_template('home/index.html', articles=Article.get_all())