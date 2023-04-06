from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Colun(db.String, unique=True, nullable=False)
    password = db.Colun(db.String, unique=True, nullable=False)
    email = db.Colun(db.String, unique=True, nullable=False)
    # 0 - Admin, 1 - Manager, 2 - Moderator, 3 - Normal user
    role = db.Colun(db.Integer, nullable=False, default=3)
    status = db.Colun(db.Boolean, default=True)
    links = db.relationship('Link', backref='user', lazy=True)
