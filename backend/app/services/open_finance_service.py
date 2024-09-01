import pandas as pd

def get_mock_data() -> dict:
    """
    Função para retornar dados mockados de Open Finance.
    """
    try:
        # Exemplo de dados mockados
        chart_data = [100, 200, 300, 400, 500]
        financial_data = [
            {"name": "Recebíveis", "value": 1000},
            {"name": "Pagáveis", "value": 800}
        ]

        # Lendo arquivos CSV como exemplo de mock data
        corporate_purchases = pd.read_csv('data/basededados/corporate_purchase.csv').to_dict(orient='records')
        transactions = pd.read_csv('data/basededados/transaction.csv').to_dict(orient='records')
        transfers = pd.read_csv('data/basededados/transfer.csv').to_dict(orient='records')
        invoices = pd.read_csv('data/basededados/invoice.csv').to_dict(orient='records')

        return {
            "chart_data": chart_data,
            "financial_data": financial_data,
            "corporate_purchases": corporate_purchases,
            "transactions": transactions,
            "transfers": transfers,
            "invoices": invoices
        }

    except FileNotFoundError as e:
        raise Exception(f"Erro ao carregar dados: {str(e)}")
