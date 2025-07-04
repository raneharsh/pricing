import numpy as np
import pandas as pd

df = pd.read_csv('data/raw/loans.csv')
np.random.seed(42)

# Add synthetic credit scores
df['credit_score'] = np.random.normal(loc=660, scale=50, size=len(df)).astype(int)
df['credit_score'] = np.clip(df['credit_score'], 500, 800)

# Define risk segments
def score_to_segment(score):
    if score >= 750: return 'Prime'
    elif score >= 680: return 'Near-Prime'
    else: return 'Subprime'

df['risk_segment'] = df['credit_score'].apply(score_to_segment)
df.to_csv('data/raw/loans.csv', index=False)
print("✅ Credit score bands and risk segments added")
