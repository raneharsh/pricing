import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_parquet('data/processed/loans.parquet')
X = df[['amount','rate_offered']]
X_scaled = StandardScaler().fit_transform(X)

kmeans = KMeans(4, random_state=1).fit(X_scaled)
df['segment'] = kmeans.labels_
df.to_csv('data/processed/segments.csv', index=False)
print("Segmentation complete")
