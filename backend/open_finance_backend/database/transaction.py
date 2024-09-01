import pandas as pd

# Atualize o caminho do diretório de dados
DATA_PATH = "data/"

def get_transactions(chunk_size=1000, skip_rows=0):
    """
    Lê o arquivo CSV de transações em chunks e retorna um chunk específico como uma lista de dicionários.
    Converte campos numéricos para strings conforme necessário.
    """
    try:
        df_chunk = pd.read_csv(f"{DATA_PATH}transaction.csv", skiprows=range(1, skip_rows), nrows=chunk_size)
        
        # Convertendo colunas específicas para string (exemplo se necessário)
        df_chunk['id'] = df_chunk['id'].astype(str)
        df_chunk['source'] = df_chunk['source'].astype(str)
        df_chunk['externalId'] = df_chunk['externalId'].astype(str)
        df_chunk['workspaceId'] = df_chunk['workspaceId'].astype(str)

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
