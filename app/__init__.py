from flask import Flask
from .db import db, migrate
from .config import Config
from flask_seeder import FlaskSeeder

def create_app():
    app = Flask(__name__)
    seeder = FlaskSeeder()
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    seeder.init_app(app, db)


    with app.app_context():
        from .models import User, Link
        from .routes import bp_user

        app.register_blueprint(bp_user)
        #seeder.add_seeder(UserSeeder)

        db.create_all()

        return app
