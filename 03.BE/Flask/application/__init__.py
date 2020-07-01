# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:23:50 2020

@author: ACMD-YYB
"""


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config['SQLALCHEMY_DATABASE_URI'] = config.alchemy_uri()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    """app.config.from_object('config.Config')"""
    app.config.from_object('config')
    db.init_app(app)

    with app.app_context():
        # Imports
        from . import routes, human, angel, inv

        # Create tables for our models
        db.create_all()

        return app