import pandas as pd

# Atualize o caminho do diretório de dados
DATA_PATH = "data/"

def get_transfers(chunk_size=1000, skip_rows=0):
    """
    Lê o arquivo CSV de transferências em chunks e retorna um chunk específico como uma lista de dicionários.
    Converte campos numéricos para strings conforme necessário.
    """
    try:
        df_chunk = pd.read_csv(f"{DATA_PATH}transfer.csv", skiprows=range(1, skip_rows), nrows=chunk_size)
        
        # Convertendo colunas específicas para string (exemplo se necessário)
        df_chunk['id'] = df_chunk['id'].astype(str)
        df_chunk['transfer_id'] = df_chunk['transfer_id'].astype(str)
        df_chunk['transfer_status'] = df_chunk['transfer_status'].astype(str)
        df_chunk['transfer_name'] = df_chunk['transfer_name'].astype(str)
        df_chunk['transfer_taxId'] = df_chunk['transfer_taxId'].astype(str)
        df_chunk['transfer_bankCode'] = df_chunk['transfer_bankCode'].astype(str)
        df_chunk['transfer_branchCode'] = df_chunk['transfer_branchCode'].astype(str)
        df_chunk['transfer_accountNumber'] = df_chunk['transfer_accountNumber'].astype(str)
        df_chunk['transfer_workspaceId'] = df_chunk['transfer_workspaceId'].astype(str)

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
