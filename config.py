import os


# default config parent class
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'my precious'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


# child class which inherits the Baseconfig settings
class DevelopmentConfig(BaseConfig):
    DEBUG = True


# child class which inherits the Baseconfig settings
class ProductionConfig(BaseConfig):
    DEBUG = False
