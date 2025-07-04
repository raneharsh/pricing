import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
from faker import Faker

# Initialize
fake = Faker()
np.random.seed(42)
num_records = 10_000

# Generate synthetic application IDs and dates
app_ids = [f"APP-{i:06d}" for i in range(1, num_records + 1)]
app_dates = [fake.date_between(start_date="-3y", end_date="today") for _ in range(num_records)]

# Loan attributes
amounts = np.round(np.random.normal(loc=8000, scale=2000, size=num_records), -2)
amounts = np.clip(amounts, 1000, 25000)
rates = np.round(np.random.normal(loc=0.18, scale=0.05, size=num_records), 4)
rates = np.clip(rates, 0.05, 0.35)

# Terms (in months)
terms = np.random.choice([24, 36, 48], size=num_records, p=[0.25, 0.5, 0.25])

# Default status: ~12% default rate
statuses = np.random.choice(['Paid', 'Default'], size=num_records, p=[0.88, 0.12])

# Payment behavior: Only for paid
payment_dates = [
    (app_date + timedelta(days=int(term * 30.5))) if status == 'Paid' else pd.NaT
    for app_date, term, status in zip(app_dates, terms, statuses)
]

# Assemble DataFrame
df = pd.DataFrame({
    'app_id': app_ids,
    'app_date': app_dates,
    'amount': amounts,
    'rate_offered': rates,
    'term_months': terms,
    'status': statuses,
    'payment_date': payment_dates
})

# Save to CSV
df.to_csv('data/raw/loans.csv', index=False)
print("✅ Synthetic loan data generated at data/raw/loans.csv")
