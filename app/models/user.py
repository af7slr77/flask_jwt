from ..db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    # 0 - Admin, 1 - Manager, 2 - Moderator, 3 - anonymous 4 - Normal user
    role = db.Column(db.Integer, nullable=False, default=4)
    status = db.Column(db.Boolean, default=True)
    links = db.relationship('Link', backref='user', lazy=True)

    def __init__(self, username, password, email, role, status):
        self.username = username
        self.password = password
        self.email = email
        self.role = role
        self.status = status
