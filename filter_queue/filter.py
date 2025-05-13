import json, sqlite3, csv
from datetime import date, timedelta
from config import CFG

def load_history(db="data/applied.db"):
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS applied(url TEXT PRIMARY KEY)")
    rows = c.execute("SELECT url FROM applied").fetchall()
    conn.close()
    return {r[0] for r in rows}

def filter_and_queue(raw_listings):
    history = load_history()
    to_apply, skipped = [], []
    today = date.today()
    for job in raw_listings:
        if job.url in history:
            continue
        if job.salary < CFG['salary_min']:
            continue
        if (today - job.date_posted).days > 30:
            continue
        if job.easy_apply:
            to_apply.append(job.__dict__)
        else:
            skipped.append(job.__dict__)

    # Write queues
    os.makedirs('data', exist_ok=True)
    with open('data/to_apply.json', 'w') as f:
        json.dump(to_apply, f, default=str)
    with open('data/skipped.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        for j in skipped:
            writer.writerow([j['date_posted'], j['title'], j['company'], j['url'], j['salary']])
