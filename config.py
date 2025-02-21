import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SERVER_PORT = 8080
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


