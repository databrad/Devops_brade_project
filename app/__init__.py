from flask import Flask
from app.config import Config, TestConfig
from app.db import init_db
from app.models import *


def create_app(config_class = None):
    app = Flask(__name__)
    app.config.from_object(config_class or Config)

    # Initialize database
    init_db(app)

    # Register blueprints
    from app.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app