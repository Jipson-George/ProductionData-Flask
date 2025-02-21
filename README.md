
## Setup
. Create virtual environment
. Install dependencies: `pip install -r requirements.txt`
. Run migrations: `flask db upgrade`
. Start server: `python main.py`

## API Endpoints
- Post (endpoint for posting data from xls/xlsx into database)  - http://127.0.0.1:8080/wells
- Get (getting Details of a specific well) -http://127.0.0.1:8080/data?well=34059242540000
