  
from flask_restful import Api
from app.resources.well_resource import WellResource

def init_routes(api: Api):
    api.add_resource(WellResource, '/data')
