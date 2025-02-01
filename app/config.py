import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    # 'mysql+pymysql://root:root@localhost:3306/product_store' , 'mysql+pymysql://brad:brad_steve@db:3306/product_store'
    print("Database URI: ", SQLALCHEMY_DATABASE_URI) 

    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
