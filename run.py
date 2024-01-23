from app import create_app
import time
import seeed_si114x
import signal
from threading import Thread
from app.utils.shared import storage_lock, shared_storage

def main_loop():
    SI1145 = seeed_si114x.grove_si114x()

    try:
        while True:
            with storage_lock:
                visible = SI1145.ReadVisible,
                uv = SI1145.ReadUV / 100,
                ir = SI1145.ReadIR

                shared_storage['visible'] = visible[0],
                shared_storage['uv'] = uv[0],
                shared_storage['ir'] = ir,
            time.sleep(1800)
    except Exception as e:
        print(f"Error reading from sensor: {e}")

app = create_app()

if __name__ == '__main__':
    signal.signal(signal.SIGTSTP, signal.SIG_IGN)
    signal.signal(signal.SIGQUIT, signal.SIG_IGN)

    thread = Thread(target=main_loop)
    thread.daemon = True  # makes the thread exit when the main thread exits.
    thread.start()

    # Use host='0.0.0.0' to make the app accessible externally 
    app.run(host='0.0.0.0', port=3000, debug=False, use_reloader=False)