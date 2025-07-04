# scripts/train_logit.py
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

df = pd.read_parquet('data/processed/loans.parquet')
df['y'] = (df['status'] == 'Default').astype(int)
X = df[['rate_offered', 'amount']]
y = df['y']

model = LogisticRegression()
model.fit(X, y)

# Save coefficients
np.save('data/processed/logit_coeff.npy', model.coef_)
np.save('data/processed/logit_intercept.npy', model.intercept_)
print("✅ Logistic regression coefficients saved")
