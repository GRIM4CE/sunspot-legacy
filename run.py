from app import create_app
import time
from seeed_si114x import grove_si114x
from threading import Thread
from app.utils.shared import storage_lock, shared_storage
from config import Config

def main_loop():
    light = grove_si114x()

    try:
        while True:
            with storage_lock:
                visible = light.ReadVisible,
                uv = light.ReadUV / 100,
                ir = light.ReadIR

                shared_storage['visible'] = visible[0],
                shared_storage['uv'] = uv[0],
                shared_storage['ir'] = ir,
            time.sleep(Config.RECORD_TIME_INTERVAL)
    except Exception as e:
        print(f"Error reading from sensor: {e}")

app = create_app()

if __name__ == '__main__':
    thread = Thread(target=main_loop)
    thread.daemon = True  # makes the thread exit when the main thread exits.
    thread.start()


    # Use host='0.0.0.0' to make the app accessible externally 
    app.run(host='0.0.0.0', port=3000, debug=False, use_reloader=False)