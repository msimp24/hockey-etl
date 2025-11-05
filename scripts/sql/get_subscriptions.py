from pathlib import Path
import logging
import sqlite3
import pandas as pd

import os
from dotenv import load_dotenv

load_dotenv()
ENV_DB_PATH = os.environ.get('DB_PATH')


BASE_DIR = Path(__file__).resolve().parent.parent.parent

if ENV_DB_PATH and Path(ENV_DB_PATH).is_absolute():
    DB_PATH = Path(ENV_DB_PATH)
else:
    DB_PATH = BASE_DIR / ENV_DB_PATH

LOG_FILE = BASE_DIR / 'logs' /'load_data_log.log'

LOG_FILE.parent.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s %(levelname)s: %(message)s',
    level=logging.INFO,
    filemode='a'  
)
logger = logging.getLogger()


def get_subscriptions_data():
    try:
        DB_PATH.parent.mkdir(parents=True, exist_ok=True) 
        
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor() 
        
        res = cursor.execute("SELECT * FROM subscriptions")
        
        subscriptions = res.fetchall()
        
        conn.close()
        
        logger.info(f"Data loaded successfully. {len(subscriptions)} rows written.")
        print(subscriptions)
        return subscriptions
    except Exception as e:
        logger.error(f"An error occurred while loading data: {e}")
        
        
if __name__ == "__main__":
    get_subscriptions_data()      