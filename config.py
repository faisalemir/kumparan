import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = "mysql://root@localhost/kumparan"

class Testing(Config):
    DEBUG = True
    TESTING = True

class Development(Config):
    DEBUG = True
    TESTING = False

class Production(Config):
    DEBUG = False
    TESTING = False

app_config = {
    "testing": Testing,
    "development": Development,
    "production": Production
}
