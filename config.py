from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    DEBUG = False
    SCHEDULER_API_ENABLED = True
    MONGO_URI = os.environ.get("MONGO_URI")
    RECORD_TIME_INTERVAL=600