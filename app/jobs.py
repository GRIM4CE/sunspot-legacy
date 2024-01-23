from .utils.extensions import scheduler
from .db import create_sunspot_record 
from datetime import datetime
from .utils.shared import shared_storage, storage_lock

def get_light_reading():
    with scheduler.app.app_context():
        try:
            with storage_lock:  # Ensure thread-safe access
                visible = shared_storage.get('visible')[0]
                uv = shared_storage.get('uv')[0]
                ir = shared_storage.get('ir')[0]
            current_datetime = datetime.utcnow()

            document = {"time": current_datetime, "visible": visible, "uv": uv, "ir": ir}

            id = create_sunspot_record(document)
        
        except (RuntimeError):
            print(RuntimeError)

scheduler.add_job(id='get_light_reading1', func=get_light_reading, trigger='interval', minutes=30)