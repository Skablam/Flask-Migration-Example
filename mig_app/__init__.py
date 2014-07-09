import os, logging
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import DevelopmentConfig

app = Flask(__name__)

app.config.from_object(DevelopmentConfig)

if not app.debug:
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)

db = SQLAlchemy(app)
