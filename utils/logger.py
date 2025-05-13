import sqlite3

def log_success(url, db='data/applied.db'):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO applied(url) VALUES (?)", (url,))
    conn.commit()
    conn.close()
