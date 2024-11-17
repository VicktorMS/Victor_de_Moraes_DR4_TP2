import pandas as pd
# 7 - Organizando a Bagunça
########################

def unificar_bases(dados_json, dados_csv, dados_txt):
    """
    Unifica os dados de diferentes bases (JSON, CSV, TXT) em um único DataFrame Pandas.

    Args:
        dados_json (str): Caminho do arquivo JSON contendo dados.
        dados_csv (str): Caminho do arquivo CSV contendo dados.
        dados_txt (str): Caminho do arquivo TXT delimitado por ponto e vírgula (;).

    Returns:
        pd.DataFrame: DataFrame com todas as bases de dados.
    """
    try:
        df_json = pd.read_json(dados_json)
        df_csv = pd.read_csv(dados_csv)
        df_txt = pd.read_csv(dados_txt, delimiter=';')

        # Unifica os dados
        df_consolidado = pd.concat([df_json, df_csv, df_txt], ignore_index=True, sort=False)

        return df_consolidado
    except Exception as e:
        raise Exception(f"Erro ao consolidar bases de dados: {e}")




def main():
    print("Esta é a questão: Organizando a Bagunça")
    arquivo_json = "src/data/INFwebNet.json"
    arquivo_csv = "src/data/INFwebNet.csv"
    arquivo_txt = "src/data/dados_usuarios_novos.txt"

    try:
        df = unificar_bases(arquivo_json, arquivo_csv, arquivo_txt)

        print(f"DataFrame Consolidado - Total de registros: {len(df)}")
        print(df.head())  # Exibe os primeiros registros como exemplo
    except Exception as e:
        print(e)