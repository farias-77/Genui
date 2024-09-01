import pandas as pd

def get_receivables() -> str:
    """
    Lê o arquivo CSV com os recebíveis, ordena pelos maiores valores mais próximos de acontecer,
    e gera um texto listando os top 5 recebíveis.

    Args:
        csv_file_path (str): O caminho para o arquivo CSV contendo os recebíveis.

    Returns:
        str: Um texto formatado com os top 5 recebíveis mais próximos e de maior valor.
    """
    csv_file_path = "./insight_generators/receivables/receivables.csv"
    df_receivables = pd.read_csv(csv_file_path)
    df_receivables["Data Prevista"] = pd.to_datetime(df_receivables["Data Prevista"])
    df_top5 = df_receivables.sort_values(by=["Data Prevista", "Valor"], ascending=[True, False]).head(5)

    texto = "Top 5 recebíveis mais próximos:\n"
    for _, row in df_top5.iterrows():
        texto += f"- Recebível {row['ID']} - Valor R$ {row['Valor']:.2f} - Data {row['Data Prevista']} - Tipo: {row['Tipo']}\n"

    return {
        "type": "buy opportunity",
        "content": texto
    }

if __name__ == "__main__":
    print(get_receivables(csv_file_path))
