from pathlib import Path
import logging
from transform import transform
import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent

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
    df = transform()
    try:
        DB_PATH.parent.mkdir(parents=True, exist_ok=True)  
        with sqlite3.connect(DB_PATH) as conn:

          cursor = conn.cursor()
        
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT OR IGNORE INTO matchups (Game_Number, Date, Time, visitor_team_id, Visitor_Goals, home_team_id, Home_Goals, Extra_Time, Attendance, Game_Duration, Completed, week_number)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                row["Game_Number"],
                row["Date"],
                row["Time"],
                row["Visitor"],
                row["Visitor_Goals"],
                row['Home'],
                row['Home_Goals'],
                row['Extra_Time'],
                row['Attendance'],
                row['Game_Duration'],
                row['Completed'], 
                row['Week_Number']
            ))
            

        conn.commit()
        conn.close()
            
            
        logger.info(f"Data loaded successfully. {len(df)} rows written.")
    except Exception as e:
        logger.error(f"An error occurred while loading data: {e}")
        

if __name__ == "__main__":
    loadData()        