import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('can_log.db')
df = pd.read_sql_query("SELECT * FROM can_logs", conn)

df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
freq = df['msg_id'].value_counts()
print("Top Frequent Messages:\n", freq.head())

if freq.empty:
    print("No CAN data found in the database. Please run the logger and send CAN messages first.")
    exit()

freq.plot(kind='bar', title='CAN Message Frequency', figsize=(8,5))
plt.xlabel("Message ID")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

df_sorted = df.sort_values(['msg_id', 'timestamp'])
df_sorted['time_diff'] = df_sorted.groupby('msg_id')['timestamp'].diff().dt.total_seconds()
missing_frames = df_sorted[df_sorted['time_diff'] > 0.1]

print("\nMissing Frame Suspicions:\n", missing_frames[['msg_id', 'timestamp', 'time_diff']].head())

