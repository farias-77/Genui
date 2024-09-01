import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

np.random.seed(42)

def generate_past_6_months_data(n_samples=1000):
    customer_names = [f'Cliente_{i}' for i in range(1, 101)]
    
    data = {
        'customer_name': np.random.choice(customer_names, n_samples),
        'amount': np.random.uniform(100, 10000, n_samples).round(2),
        'due_date': [datetime.now().date() - timedelta(days=np.random.randint(0, 180)) for _ in range(n_samples)]
    }
    
    df = pd.DataFrame(data)
    
    df['label'] = df['customer_name'].apply(lambda x: 'late' if int(x.split('_')[1]) % 5 == 0 else 'regular')
    
    df = df.sort_values('due_date')
    
    return df

def generate_next_week_data(n_samples=1000):
    customer_names = [f'Cliente_{i}' for i in range(1, 101)]
    
    data = {
        'customer_name': np.random.choice(customer_names, n_samples),
        'amount': np.random.uniform(100, 10000, n_samples).round(2),
        'due_date': [datetime.now().date() + timedelta(days=np.random.randint(0, 7)) for _ in range(n_samples)]
    }
    
    df = pd.DataFrame(data)
    
    df = df.sort_values('due_date')
    
    return df

df_past_6_months = generate_past_6_months_data(50000)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename_past_6_months = f"synthetic_payment_data_past_6_months.csv"

if not os.path.exists(filename_past_6_months):
    df_past_6_months.to_csv(filename_past_6_months, index=False)
    print(f"Dados sintéticos dos últimos 6 meses gerados e salvos em {filename_past_6_months}")
else:
    print(f"O arquivo {filename_past_6_months} já existe. Pulando a geração.")

print(f"Total de registros: {len(df_past_6_months)}")
print("\nPrimeiras 5 linhas do dataset:")
print(df_past_6_months.head())
print("\nDistribuição de labels:")
print(df_past_6_months['label'].value_counts(normalize=True))

df_next_week = generate_next_week_data(20)

filename_next_week = f"synthetic_payment_data_next_week.csv"

if not os.path.exists(filename_next_week):
    df_next_week.to_csv(filename_next_week, index=False)
    print(f"\nDados sintéticos de pagamentos devidos na próxima semana gerados e salvos em {filename_next_week}")
else:
    print(f"O arquivo {filename_next_week} já existe. Pulando a geração.")

print(f"Total de registros: {len(df_next_week)}")
print("\nPrimeiras 5 linhas do dataset:")
print(df_next_week.head())
