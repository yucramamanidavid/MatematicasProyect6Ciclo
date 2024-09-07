# config.py

from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mysecretkey')
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG', True)
    SERVER_NAME = os.environ.get('SERVER_NAME', 'localhost:5000')
    TOLERANCE = float(os.environ.get('TOLERANCE', 0.01))
    MAX_ITER = int(os.environ.get('MAX_ITER', 50))
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'uploads')
    ALLOWED_EXTENSIONS = os.environ.get('ALLOWED_EXTENSIONS', 'txt,csv').split(',')
