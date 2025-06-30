import can
import sqlite3

conn = sqlite3.connect('can_log.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS can_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp REAL,
    msg_id TEXT,
    data_bytes TEXT
)
''')
conn.commit()

bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

print("Logging CAN messages... (Press Ctrl+C to stop)")
try:
    for msg in bus:
        timestamp = msg.timestamp
        msg_id = hex(msg.arbitration_id)
        data = msg.data.hex()

        cursor.execute("INSERT INTO can_logs (timestamp, msg_id, data_bytes) VALUES (?, ?, ?)",
                       (timestamp, msg_id, data))
        conn.commit()

except KeyboardInterrupt:
    print("Logging stopped.")
finally:
    conn.close()

