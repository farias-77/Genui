import pandas as pd

# Atualize o caminho do diretório de dados
DATA_PATH = "data/"

def get_corporate_purchases(chunk_size=1000, skip_rows=0):
    """
    Lê o arquivo CSV de compras corporativas em chunks e retorna um chunk específico como uma lista de dicionários.
    Converte campos numéricos para strings conforme necessário.
    """
    try:
        df_chunk = pd.read_csv(f"{DATA_PATH}corporate-purchase.csv", skiprows=range(1, skip_rows), nrows=chunk_size)
        
        # Convertendo colunas específicas para string
        df_chunk['purchase_cardId'] = df_chunk['purchase_cardId'].astype(str)
        df_chunk['purchase_id'] = df_chunk['purchase_id'].astype(str)
        df_chunk['purchase_holderId'] = df_chunk['purchase_holderId'].astype(str)
        df_chunk['purchase_workspaceId'] = df_chunk['purchase_workspaceId'].astype(str)

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
