import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    USER = os.getenv('DB_USER', 'me')
    PASSWORD = os.getenv('DB_PASSWORD', 'me')
    HOST = os.getenv('DB_HOST', 'localhost')
    PORT = os.getenv('DB_PORT', '3306')
    DATABASE = os.getenv('DB_NAME', 'mydatabase')

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("DATABASE_URL is not set correctly")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
