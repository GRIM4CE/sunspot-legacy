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
        cursor = db.sunspot_records.find({}, { 'time': 1, 'visible': 1, 'uv': 1, 'ir': 1, '_id': 0})
        data_list = []
        for doc in cursor:
            # Format the datetime object to a string
            formatted_time = doc['time'].strftime('%m/%d/%Y %H:%M')

            # Create a new dictionary with the formatted time
            formatted_doc = {
                'time': formatted_time,
                'visible': doc['visible'],
                'uv': doc['uv'],
                'ir': doc['ir'],
            }

            data_list.append(formatted_doc)
        
        return data_list
    except Exception as e:
        raise e 
    
def create_sunspot_record(data):
    try:
        inserted_id = db.sunspot_records.insert_one(data).inserted_id
        return inserted_id
    except Exception as e:
        raise e 
    
def drop_records():
    try:
        deleted_count = db.sunspot_records.delete_many({}).deleted_count
        return deleted_count
    except Exception as e:
        raise e 