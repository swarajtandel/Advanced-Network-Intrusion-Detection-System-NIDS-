import sqlite3
import logging
from prometheus_client import Counter

logging.basicConfig(filename='ids.log', level=logging.INFO)

# Prometheus counters
alert_counter = Counter('nids_alerts_total', 'Total NIDS alerts', ['type'])

class AlertManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS alerts
                             (ts DATETIME DEFAULT CURRENT_TIMESTAMP, type TEXT, info TEXT)''')

    def raise_alert(self, alert_type, info, pkt):
        logging.info(f"{alert_type.upper()} alert: {info}")
        self.conn.execute("INSERT INTO alerts(type, info) VALUES(?, ?)", (alert_type, info))
        self.conn.commit()
        alert_counter.labels(type=alert_type).inc()