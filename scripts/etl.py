import pandas as pd
import sqlite3
import os

# Load from SQLite
conn = sqlite3.connect('db/loans.db')
df = pd.read_sql_query("SELECT * FROM loans", conn)
conn.close()

# Clean & QC
assert df['amount'].notnull().all(), "Missing loan amount"
df['rate_offered'] = df['rate_offered'].fillna(df['rate_offered'].median())

# Ensure output directory exists
os.makedirs('data/processed', exist_ok=True)

# Save
df.to_parquet('data/processed/loans.parquet', index=False)
print("✅ ETL complete")
