import pandas as pd
import pytz
from datetime import datetime

invoices_data_path = "./resource/invoice.csv"
invoices_log_data_path = "./resource/invoice-log.csv"
year = 2024
month = 8
day = 20
discount_rate = 0.02
due_days_threshold = 15

def read_data(invoices_path):
    invoices = pd.read_csv(invoices_path)
    return invoices

def preprocess_data(invoices, year, month, day):
    invoices['created'] = pd.to_datetime(invoices['created'], errors='coerce')
    invoices['due'] = pd.to_datetime(invoices['due'], errors='coerce')
    invoices['expiration'] = pd.to_datetime(invoices['expiration'], errors='coerce')
    invoices_clean = invoices.dropna(subset=['created', 'due', 'expiration'])

    # Data de referência
    now_utc = pd.Timestamp(year=year, month=month, day=day, hour=0, minute=0, second=0, tz='UTC')
    invoices_clean['days_to_due'] = (invoices_clean['due'] - now_utc).dt.days
    
    # Filtrar apenas faturas com vencimento futuro
    invoices_clean = invoices_clean[invoices_clean['days_to_due'] >= 0]
    
    return invoices_clean

def categorize_eligibility(row, due_days_threshold):
    if row['days_to_due'] <= due_days_threshold and (row['fine'] > 0 or row['interest'] > 0):
        return "elegível"
    else:
        return "não elegível"

def calculate_savings(invoices_clean, discount_rate):
    invoices_clean['discount_amount'] = invoices_clean['amount'] * discount_rate
    invoices_clean['total_savings'] = invoices_clean['discount_amount'] + invoices_clean['fine'] + invoices_clean['interest']
    return invoices_clean

def generate_insight(row):
    return (f"A fatura {row['id']} de R$ {row['amount']:.2f} que vence em {row['days_to_due']} dias "
            f"é elegível para antecipação. Ao antecipar o pagamento, você poderá economizar "
            f"R$ {row['total_savings']:.2f}, evitando multas e juros. Recomendamos usar essa "
            f"economia para reinvestir no seu negócio ou fortalecer o capital de giro.")

def apply_insight_generation(invoices_clean, due_days_threshold):
    invoices_clean['eligibility'] = invoices_clean.apply(categorize_eligibility, axis=1, due_days_threshold=due_days_threshold)
    eligible_invoices = invoices_clean[invoices_clean['eligibility'] == "elegível"]
    eligible_invoices['insight'] = eligible_invoices.apply(generate_insight, axis=1)
    return eligible_invoices

def select_invoices(eligible_invoices):
    random_5_invoices = eligible_invoices.sample(n=5, random_state=42)  
    
    random_5_invoices_sorted = random_5_invoices.sort_values(by='total_savings', ascending=False)
    
    summary = "As 5 faturas abaixo poderiam ser antecipadas: "
    for index, row in random_5_invoices_sorted.iterrows():
        summary += (f"\n- Fatura {row['id']} que vence em {row['due'].strftime('%Y-%m-%d')}, "
                    f"com total saving de R$ {row['total_savings']:.2f}.")
    
    return summary

def get_early_invoice_insight():
    print("cheguei aqui vai tomar no cu allan")
    invoices = read_data(invoices_data_path)
    invoices_clean = preprocess_data(invoices, year, month, day)
    invoices_clean = calculate_savings(invoices_clean, discount_rate)
    eligible_invoices = apply_insight_generation(invoices_clean, due_days_threshold)
    early_invoice_insight = select_invoices(eligible_invoices)
    
    return early_invoice_insight

if __name__ == "__main__":
    print(get_early_invoice_insight())