import pandas as pd
import numpy as np
from datetime import datetime, timedelta

num_receivables = 30
base_date = datetime(2024, 9, 30)

data = {
    "ID": [f"REC{i:05d}" for i in range(1, num_receivables + 1)],
    "Valor": np.round(np.random.uniform(1000, 50000, num_receivables), 2),
    "Data Prevista": [(base_date + timedelta(days=np.random.randint(0, 60))).strftime('%Y-%m-%d') for _ in range(num_receivables)],
    "Tipo": ["Vale refeição"] * num_receivables
}

df_receivables = pd.DataFrame(data)
df_receivables.to_csv("receivables.csv", index=False)
