from flask_restful import Resource
from flask import request
import pandas as pd
from app.models import Production
from app.database  import db
import io

class WellResource(Resource):
    def get(self):
        well_number = request.args.get('well')
        
        if not well_number:
            return {"error": "Well number is required"}, 400
        
        production = Production.get_by_well_number(well_number)
        
        if production:
            return {
                "oil": production.oil,
                "gas": production.gas,
                "brine": production.brine
            }
        
        return {"error": "Well not found"}, 404

    def post(self):
        try:
            if 'file' not in request.files:
                return {"error": "No file uploaded"}, 400

            file = request.files['file']
            if not file.filename.endswith('.xls') and not file.filename.endswith('.xlsx'):
                return {"error": "Please upload an Excel file"}, 400
            df = pd.read_excel(file)
            df.columns = df.columns.str.strip() 
            df.columns = df.columns.str.replace(r'\s+', ' ', regex=True)  
            df.columns = df.columns.str.upper()  
            print("Updated Column Names:", df.columns.tolist())

            annual_data = df.groupby('API WELL NUMBER').agg({
                'OIL': 'sum',
                'GAS': 'sum',
                'BRINE': 'sum'
            }).reset_index()
            Production.query.delete()
            for _, row in annual_data.iterrows():
                production = Production(
                    api_well_number=str(row['API WELL NUMBER']),
                    oil=int(row['OIL']),
                    gas=int(row['GAS']),
                    brine=int(row['BRINE'])
                )
                db.session.add(production)

            db.session.commit()
            return {"message": "Data processed successfully"}, 201

        except Exception as e:
            print("Error:", str(e))
            db.session.rollback()
            return {"error": str(e)}, 500

