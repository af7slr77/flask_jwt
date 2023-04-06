from flask import Flask
from .db import db, migrate
from .config import Config


def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    with app.app_context():
        from .routes import bp_user

        app.register_blueprint(bp_user)

        db.create_all()

        return app
