"""
Getting the bot workers to clean all the raw data to store them in MYSQL
"""
from app.Bots.workers.GlobalForest_worker import start_global
from app.Bots.workers.Matter_worker import start_matter

import threading

matter_thread = threading.Thread(target=start_matter)
global_thread = threading.Thread(target=start_global)

matter_thread.start()
global_thread.start()   

matter_thread.join()
global_thread.join()