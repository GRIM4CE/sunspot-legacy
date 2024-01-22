from .extensions import scheduler
from .utils import incrementJSONFileNumber

def counter():
    print('hi')
    file_path = "./temp/data.json"
    incrementJSONFileNumber(file_path)

scheduler.add_job(id='counter1', func=counter, trigger='interval', minutes=1)