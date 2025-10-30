from pathlib import Path
import logging
from scripts.transform import transform_matchups
import sqlite3

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

def loadData():
    df = transform_matchups()
    try:
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)  
        with sqlite3.connect(DB_PATH) as conn:
            df.to_sql(con=conn, name="matchups", if_exists='replace')
            

            
            
        logger.info(f"Data loaded successfully. {len(df)} rows written.")
    except Exception as e:
        logger.error(f"An error occurred while loading data: {e}")
        

if __name__ == "__main__":
    loadData()        