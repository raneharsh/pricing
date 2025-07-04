import pandas as pd
import sqlite3

df = pd.read_csv('data/raw/loans.csv', parse_dates=['app_date', 'payment_date'])
conn = sqlite3.connect('db/loans.db')
df.to_sql('loans', conn, if_exists='replace', index=False)
conn.commit()
conn.close()
print("Data loaded into SQLite")
