import sqlite3

conn = sqlite3.connect('db/loans.db')
with open('sql/create_tables.sql', 'r') as f:
    conn.executescript(f.read())
conn.commit()
conn.close()
