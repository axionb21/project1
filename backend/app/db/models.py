
CREATE_LOG_TABLE = '''
CREATE TABLE IF NOT EXISTS prediction_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    amount REAL,
    category TEXT,
    user_type TEXT,
    region TEXT,
    score REAL,
    confidence REAL,
    week INTEGER
)
'''
