"""
Utility Functions
"""

import sqlite3
import requests

def setup_database(db_name="network_logs.db"):
    """
    Setup SQLite database
    
    Args:
        db_name: Nama file database
    
    Returns:
        Database connection
    """
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS devices
                 (mac TEXT PRIMARY KEY,
                  ip TEXT,
                  vendor TEXT,
                  first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    return conn

def send_alert(message, token, chat_id):
    """
    Kirim alert ke Telegram
    
    Args:
        message: Pesan yang dikirim
        token: Bot token
        chat_id: Chat ID tujuan
    """
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "HTML"
        }
        requests.post(url, json=payload, timeout=3)
    except:
        pass  # Silent fail

def get_vendor(mac):
    """
    Cek vendor dari MAC address (pake API publik)
    
    Args:
        mac: MAC address
    
    Returns:
        String vendor name
    """
    # TODO: Implement MAC vendor lookup API
    return "Unknown"
