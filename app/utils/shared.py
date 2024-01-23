import threading

# Initialize shared storage and its lock
shared_storage = {}
storage_lock = threading.Lock()