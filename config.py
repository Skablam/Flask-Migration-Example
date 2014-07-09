import os

class Config(object):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

    URI = 'localhost:5432'
    DB = 'foodb'
    USER = 'foouser'
    PASS = 'password'

    # format is dialect+driver://username:password@host:port/database
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://%s:%s@%s/%s" %  (USER, PASS, URI, DB)
