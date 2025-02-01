from flask import Flask
from app.config import Config, TestConfig
from app.db import init_db
from app.models import *
from flask_cors import CORS
from flask_cors import CORS

def create_app(config_class = None):
    app = Flask(__name__)
    app.config.from_object(config_class or Config)

    # Initialize database
    init_db(app)

    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

    # Register blueprints
    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app


# from app.db import db
# from app.models import Product  # Import the model explicitly

# def create_app(config_class=None):
#     app = Flask(__name__)
#     app.config.from_object(config_class or Config)

#     # Initialize database
#     init_db(app)

#     # Create tables explicitly
#     with app.app_context():
#         db.create_all()

#     # Register blueprints
#     from app.routes import bp as routes_bp
#     app.register_blueprint(routes_bp)

#     return app
