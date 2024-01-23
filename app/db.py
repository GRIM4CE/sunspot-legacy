from flask import current_app, g
from werkzeug.local import LocalProxy
from flask_pymongo import PyMongo
from datetime import datetime

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = PyMongo(current_app).db
       
    return db

# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)

def get_sunspot():
    try:
        cursor = db.sunspot_records.find()
        data_list = [doc for doc in cursor]
        return data_list
    except Exception as e:
        raise e 
    
def create_sunspot_record():
    try:
        current_datetime = datetime.now()
        inserted_id = db.sunspot_records.insert_one({"time": current_datetime, "count": db.sunspot_records.count_documents({}) + 1}).inserted_id
        return inserted_id
    except Exception as e:
        raise e 
    
def drop_records():
    try:
        deleted_count = db.sunspot_records.delete_many({}).deleted_count
        return deleted_count
    except Exception as e:
        raise e 