from .extensions import scheduler
from .db import create_sunspot_record 

def counter():
    with scheduler.app.app_context():
        try:
            id = create_sunspot_record()
            print(id)
            
        except (RuntimeError):
            print(RuntimeError)

scheduler.add_job(id='counter1', func=counter, trigger='interval', seconds=15)