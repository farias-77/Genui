import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

model_filename = 'payment_classification_model.pkl'
model = joblib.load(model_filename)

le_customer = LabelEncoder()

def load_and_prepare_data(file_path, reference_date_str="2024-01-01"):
    df = pd.read_csv(file_path)
    df["due_date"] = pd.to_datetime(df["due_date"])
    
    df["customer_name"] = le_customer.fit_transform(df["customer_name"])
    
    reference_date = pd.Timestamp(reference_date_str)
    df["days_since_reference"] = (df["due_date"] - reference_date).dt.days
    
    X = df[["customer_name", "amount", "days_since_reference"]]
    df["prediction"] = model.predict(X)
    
    return df

def get_top_5_clients_with_most_late_records(df):
    late_records = df[df["label"] == "late"]
    
    late_counts = late_records["customer_name"].value_counts().head(5)
    
    insight = """Na próxima semana, você tem pagamentos a receber dos clientes abaixo que possuem 
    alto risco de inadimplência com mais registros de atraso:\n"""
    for customer_name, count in late_counts.items():
        insight += f"- Cliente {customer_name} com {count} registros de atraso.\n"
    
    return insight

def get_default_insight():
    file_path = "synthetic_payment_data_past_6_months.csv"
    df = load_and_prepare_data(file_path)
    default_insight = get_top_5_clients_with_most_late_records(df)
    return default_insight

if __name__ == "__main__":
    insight = get_default_insight()
    print(insight)
