from pathlib import Path
import logging
import sqlite3
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent.parent

DB_PATH = BASE_DIR / 'data' / 'hockey-data.db'

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
        
        return subscriptions
    except Exception as e:
        logger.error(f"An error occurred while loading data: {e}")
        
        
if __name__ == "__main__":
    get_subscriptions_data()      