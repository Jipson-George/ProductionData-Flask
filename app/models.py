  
from .database import db

class Production(db.Model):
    __tablename__ = 'annual_production'
    
    id = db.Column(db.Integer, primary_key=True)
    api_well_number = db.Column(db.String(20), unique=True, nullable=False)
    oil = db.Column(db.Integer)
    gas = db.Column(db.Integer)
    brine = db.Column(db.Integer)
    
    @staticmethod
    def get_by_well_number(well_number):
        return Production.query.filter_by(api_well_number=well_number).first()
