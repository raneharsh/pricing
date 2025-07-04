DROP TABLE IF EXISTS loans;

CREATE TABLE loans (
    app_id TEXT PRIMARY KEY,
    app_date TEXT,
    amount REAL,
    rate_offered REAL,
    status TEXT,
    payment_date TEXT
);
