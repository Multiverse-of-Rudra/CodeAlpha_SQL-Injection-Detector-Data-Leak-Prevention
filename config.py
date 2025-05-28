import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASS = os.getenv('DB_PASS', '8303')
    DB_NAME = os.getenv('DB_NAME', 'securedb')
    AES_KEY = os.getenv('AES_KEY', 'kTrSO2drHHtTc9a7lE4yW3kROnYLhqDVzKqDg/VQAQ0=')
    CAPABILITY_TOKEN = os.getenv('CAP_TOKEN', 'Q7YtYoVlmNeXsjNH4D3LReEofvhx-3z3PVbVu2Vvt_o')
