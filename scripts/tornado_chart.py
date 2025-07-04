# tornado_chart.py
import pandas as pd
import matplotlib.pyplot as plt

# Load results
df_results = pd.read_csv('data/processed/sensitivity_results.csv')  # or wherever you saved it

# Sort and plot
df_sorted = df_results.sort_values('Total Order ST', ascending=True)

plt.figure(figsize=(8, 5))
plt.barh(df_sorted['Parameter'], df_sorted['Total Order ST'], color='skyblue')
plt.xlabel('Total Sensitivity (ST)')
plt.title('Tornado Chart: Profit Sensitivity by Variable')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('data/processed/tornado_chart.png')
plt.show()
