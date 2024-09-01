import pandas as pd

# Atualize o caminho do diretório de dados
DATA_PATH = "data/"

def get_invoices(chunk_size=1000, skip_rows=0):
    """
    Lê o arquivo CSV de faturas em chunks e retorna um chunk específico como uma lista de dicionários.
    Converte campos numéricos para strings conforme necessário.
    """
    try:
        df_chunk = pd.read_csv(f"{DATA_PATH}invoice.csv", skiprows=range(1, skip_rows), nrows=chunk_size)
        
        # Convertendo colunas específicas para string (exemplo se necessário)
        df_chunk['id'] = df_chunk['id'].astype(str)
        df_chunk['invoice_id'] = df_chunk['invoice_id'].astype(str)
        df_chunk['invoice_status'] = df_chunk['invoice_status'].astype(str)
        df_chunk['invoice_name'] = df_chunk['invoice_name'].astype(str)
        df_chunk['invoice_taxId'] = df_chunk['invoice_taxId'].astype(str)
        df_chunk['invoice_workspaceId'] = df_chunk['invoice_workspaceId'].astype(str)
        df_chunk['invoice_brcode'] = df_chunk['invoice_brcode'].astype(str)

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
