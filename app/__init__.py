from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from app.database import db
from app.routes import init_routes
from app.models import *  
from app.resources import * 

def create_app():
    app = Flask(__name__)
    app.config['SERVER_PORT'] = 8080
    api = Api(app)
    
    # SQLite configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///production.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    Migrate(app, db)
    
    init_routes(api)
    
    return app
