from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    # Create flask app
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    # Init database
    db.init_app(app)

    from .views import main
    # Import the view and register it to the flask app
    app.register_blueprint(main)

    return app