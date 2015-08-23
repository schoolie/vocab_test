# Embedded file name: C:\Development\routeless-server\routeless\__init__.py
from flask import Flask, jsonify, request

from vocab_test.extensions import db
from vocab_test.views import main
from vocab_test.models import Word
from config import config

import pdb

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    db.init_app(app)
    
    app.register_blueprint(main)
    
    return app
    
    