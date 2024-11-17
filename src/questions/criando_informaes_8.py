from .organizando_a_baguna_7 import unificar_bases
import pandas as pd
from datetime import datetime
# 8 - Criando Informações
########################

def calcular_ano_nascimento(df):
    """
    Adiciona uma nova coluna 'ano_nascimento' ao DataFrame com base na coluna 'Idade'.

    Args:
        df (pd.DataFrame): DataFrame contendo a coluna 'Idade'.

    Returns:
        pd.DataFrame: DataFrame atualizado com a nova coluna 'ano_nascimento'.
    """
    try:
        ano_atual = datetime.now().year
        df['ano_nascimento'] = pd.to_numeric(df['Idade'], errors='coerce').apply(
            lambda idade: ano_atual - int(idade) if not pd.isna(idade) else None
        )
        return df
    except Exception as e:
        raise Exception(f"Erro ao calcular ano de nascimento: {e}")

def unificar_e_criar_infos(dados_json, dados_csv, dados_txt):
    """
    Unifica os dados de diferentes fontes e adiciona uma nova coluna 'ano_nascimento'.

    Args:
        dados_json (str): Caminho do arquivo JSON.
        dados_csv (str): Caminho do arquivo CSV.
        dados_txt (str): Caminho do arquivo TXT delimitado por ponto e vírgula (;).

    Returns:
        pd.DataFrame: DataFrame atualizado.
    """
    try:
        df = unificar_bases(dados_json, dados_csv, dados_txt)

        # Adicionar a coluna 'ano_nascimento'
        df = calcular_ano_nascimento(df)

        return df
    except Exception as e:
        raise Exception(f"Erro ao consolidar dados e criar informações: {e}")

def main():
    print("Esta é a questão: Criando Informações")
    arquivo_json = "src/data/INFwebNet.json"
    arquivo_csv = "src/data/INFwebNet.csv"
    arquivo_txt = "src/data/dados_usuarios_novos.txt"

    try:
        df = unificar_e_criar_infos(arquivo_json, arquivo_csv, arquivo_txt)

        print(f"DataFrame Atualizado - Total de registros: {len(df)}")
        print(df.head())  # Exibe os primeiros registros como exemplo
    except Exception as e:
        print(e)