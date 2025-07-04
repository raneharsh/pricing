from SALib.sample import sobol
from SALib.analyze import sobol as sobol_analyze
import numpy as np
import pandas as pd

# Define problem with 4 variables
problem = {
    'num_vars': 4,
    'names': ['rate', 'term_months', 'amount', 'credit_score'],
    'bounds': [
        [0.08, 0.30],
        [24, 48],
        [2000, 20000],
        [500, 800]
    ]
}

param_values = sobol.sample(problem, 1024)

def simulate_profit(inputs):
    rate, term, amount, score = inputs
    # Risk increases with lower score and longer term
    default_risk = 0.10 + 0.005 * (rate - 0.18) + 0.002 * (term - 36) + 0.0005 * (660 - score)
    default_risk = np.clip(default_risk, 0.05, 0.35)
    revenue = rate / 12 * amount
    expected_loss = default_risk * amount * 0.4
    return revenue - expected_loss

Y = np.array([simulate_profit(x) for x in param_values])
Si = sobol_analyze.analyze(problem, Y)

df_results = pd.DataFrame({
    'Parameter': problem['names'],
    'First Order S1': Si['S1'],
    'Total Order ST': Si['ST']
})
print(df_results.round(4))
df_results.to_csv('data/processed/sensitivity_results.csv', index=False)
