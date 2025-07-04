import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

df = pd.read_parquet('data/processed/loans.parquet')
df['y'] = (df.status=='Default').astype(int)
features = ['rate_offered','amount']
X_train, X_test, y_train, y_test = train_test_split(df[features],df.y,test_size=0.3, random_state=42)

model = XGBClassifier(n_estimators=100, max_depth=4)
model.fit(X_train,y_train)
auc = roc_auc_score(y_test, model.predict_proba(X_test)[:,1])
print(f"AUC: {auc:.3f}")
model.save_model('data/processed/xgb_model.json')
