
from app.db.database import get_connection
from app.db.models import CREATE_LOG_TABLE
import datetime

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CREATE_LOG_TABLE)
    conn.commit()
    conn.close()

def insert_prediction(amount, category, user_type, region, score, confidence, week):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO prediction_logs
    (timestamp, amount, category, user_type, region, score, confidence, week)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''',(
        str(datetime.datetime.utcnow()),
        amount,
        category,
        user_type,
        region,
        score,
        confidence,
        week
    ))

    conn.commit()
    conn.close()
