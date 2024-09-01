import pandas as pd

DATA_PATH = "data/"

def get_corporate_purchases(chunk_size=1000, skip_rows=0):
    """
    Lê o arquivo CSV de compras corporativas em chunks e retorna um chunk específico como uma lista de dicionários.

    :param chunk_size: Número de linhas a serem lidas por chunk.
    :param skip_rows: Número de linhas a serem ignoradas do início do arquivo.
    :return: Lista de dicionários contendo dados do chunk.
    """
    try:
        df_chunk = pd.read_csv(f"{DATA_PATH}corporate_purchase.csv", skiprows=range(1, skip_rows), nrows=chunk_size)
        return df_chunk.to_dict(orient='records')
    except FileNotFoundError:
        print("Erro: O arquivo 'corporate_purchase.csv' não foi encontrado.")
        return []
    except pd.errors.ParserError:
        print("Erro ao analisar o arquivo CSV.")
        return []
    except Exception as e:
        print(f"Erro desconhecido: {e}")
        return []

def get_transactions(chunk_size=1000, skip_rows=0):
    """
    Lê o arquivo CSV de transações em chunks e retorna um chunk específico como uma lista de dicionários.
    """
    try:
        df_chunk = pd.read_csv(f"{DATA_PATH}transaction.csv", skiprows=range(1, skip_rows), nrows=chunk_size)
        return df_chunk.to_dict(orient='records')
    except FileNotFoundError:
        print("Erro: O arquivo 'transaction.csv' não foi encontrado.")
        return []
    except pd.errors.ParserError:
        print("Erro ao analisar o arquivo CSV.")
        return []
    except Exception as e:
        print(f"Erro desconhecido: {e}")
        return []

def get_transfers(chunk_size=1000, skip_rows=0):
    """
    Lê o arquivo CSV de transferências em chunks e retorna um chunk específico como uma lista de dicionários.
    """
    try:
        df_chunk = pd.read_csv(f"{DATA_PATH}transfer.csv", skiprows=range(1, skip_rows), nrows=chunk_size)
        return df_chunk.to_dict(orient='records')
    except FileNotFoundError:
        print("Erro: O arquivo 'transfer.csv' não foi encontrado.")
        return []
    except pd.errors.ParserError:
        print("Erro ao analisar o arquivo CSV.")
        return []
    except Exception as e:
        print(f"Erro desconhecido: {e}")
        return []

def get_invoices(chunk_size=1000, skip_rows=0):
    """
    Lê o arquivo CSV de faturas em chunks e retorna um chunk específico como uma lista de dicionários.
    """
    try:
        df_chunk = pd.read_csv(f"{DATA_PATH}invoice.csv", skiprows=range(1, skip_rows), nrows=chunk_size)
        return df_chunk.to_dict(orient='records')
    except FileNotFoundError:
        print("Erro: O arquivo 'invoice.csv' não foi encontrado.")
        return []
    except pd.errors.ParserError:
        print("Erro ao analisar o arquivo CSV.")
        return []
    except Exception as e:
        print(f"Erro desconhecido: {e}")
        return []
