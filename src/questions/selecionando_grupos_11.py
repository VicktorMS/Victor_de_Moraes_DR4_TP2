import pandas as pd
# 11 - Selecionando Grupos
########################

def salvar_grupos_por_estado(df, diretorio_saida="src/data/grupos_estados"):
    """
    Filtra os INFNETianos pelo estado onde moram e salva cada grupo em arquivos CSV separados.

    Args:
        df (pd.DataFrame): DataFrame contendo os dados dos INFNETianos, incluindo a coluna 'Estado'.
        diretorio_saida (str): Diretório onde os arquivos CSV serão salvos.
    """
    import os

    os.makedirs(diretorio_saida, exist_ok=True)

    try:
        if 'Estado' not in df.columns:
            raise ValueError("A coluna 'Estado' não está presente no DataFrame.")

        estados_unicos = df['Estado'].dropna().unique()
        for estado in estados_unicos:
            if estado == 'N/A':
                continue
            df_estado = df[df['Estado'] == estado]

            nome_arquivo = f"{diretorio_saida}/grupo_{estado}.csv"

            df_estado.to_csv(nome_arquivo, index=False, encoding='utf-8')
            print(f"Grupo do estado {estado} salvo em: {nome_arquivo}")

    except Exception as e:
        raise Exception(f"Erro ao salvar os grupos por estado: {e}")

def main():
    print("Esta é a questão: Selecionando Grupos")
    data_json = 'src/data/INFwebNet_Data.json'

    try:
        df = pd.read_json(data_json)

        salvar_grupos_por_estado(df)
    except Exception as e:
        print(e)
