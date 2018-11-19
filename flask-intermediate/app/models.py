from app import db
from datetime import datetime


class Article(db.Model):

    __tablename__ = "articles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, unique=False, nullable=False)
    author = db.Column(db.String, unique=False, nullable=True, default="John / Jane Doe")

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def json(self):
        return {'title': self.title, 'author': self.author}

    @staticmethod
    def get_all():
        return [Article.json(article) for article in Article.query.all()]

    @property
    def serialize(self):
        return {'article': {'author': self.author, 'title': self.title}}


