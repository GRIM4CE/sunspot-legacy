from .extensions import scheduler
from .db import create_sunspot_record 
from datetime import datetime

def counter():
    with scheduler.app.app_context():
        try:
            current_datetime = datetime.now()
            id = create_sunspot_record({"time": current_datetime, "count": 1})
            print(id)
            
        except (RuntimeError):
            print(RuntimeError)

scheduler.add_job(id='counter1', func=counter, trigger='interval', minutes=1)