import numpy as np
import pandas as pd

df = pd.read_parquet('data/processed/loans.parquet')
coef = np.load('data/processed/logit_coeff.npy')[0]
intercept = np.load('data/processed/logit_intercept.npy')[0]

def profit(rate):
    X = pd.DataFrame({'rate_offered': rate, 'amount': df['amount']})
    log_odds = intercept + coef[0]*X['rate_offered'] + coef[1]*X['amount']
    p_default = 1 / (1 + np.exp(-log_odds))
    expected_loss = p_default * df['amount'] * 0.4
    revenue = rate / 12 * df['amount']
    return (revenue - expected_loss).sum()

rates = np.linspace(0.08, 0.30, 12)
results = [(r, profit(r)) for r in rates]
pd.DataFrame(results, columns=['rate', 'profit']).to_csv('data/processed/profit_curve.csv', index=False)
print("✅ Pricing simulation complete")
