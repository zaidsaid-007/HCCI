from os import environ
from .config import DevelopmentConfig, ProductionConfig
from flask import Flask

app = Flask(__name__)

if environ.get('FLASK_ENV') == 'Development':
    app.config.from_object(DevelopmentConfig)
else:
    app.config.from_object(ProductionConfig)
