from ..db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    # 0 - Admin, 1 - Manager, 2 - Moderator, 3 - Normal user
    role = db.Column(db.Integer, nullable=False, default=3)
    status = db.Column(db.Boolean, default=True)
    links = db.relationship('Link', backref='user', lazy=True)
