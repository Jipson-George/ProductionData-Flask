from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from app.database import db
from app.routes import init_routes
from app.models import *  
from app.resources import *
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    api = Api(app)
    
    db.init_app(app)
    Migrate(app, db)
    
    init_routes(api)
    
    return app

