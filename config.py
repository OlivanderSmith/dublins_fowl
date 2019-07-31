import os


# default config parent class
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "\x96\xdd\K\xd4Y\x8f\xba\xa3\xc8\xce>E\tJ?w\x15\xf2\xeaS\xa1xdc"
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


# child class which inherits the Baseconfig settings
class DevelopmentConfig(BaseConfig):
    DEBUG = True


# child class which inherits the Baseconfig settings
class ProductionConfig(BaseConfig):
    DEBUG = False
