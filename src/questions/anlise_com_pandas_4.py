import pandas as pd
from utils.constants import DATA_PATH
# 4 - Análise com Pandas
########################

def calcular_media_idade(json_file):
    """
    Calcula a média de idade dos INFNETianos a partir de um arquivo JSON.

    Args:
        json_file (str): Caminho do arquivo JSON contendo os dados dos INFNETianos.

    Returns:
        float: Média de idade dos INFNETianos.
    """
    try:
        df = pd.read_json(json_file)

        # Converter a coluna 'Idade' para tipo nuérico (ignorar erros)
        df['Idade'] = pd.to_numeric(df['Idade'], errors='coerce')

        # Calcula a média de idade
        media_idade = df['Idade'].mean()

        return media_idade
    except FileNotFoundError:
        raise FileNotFoundError(f"O arquivo {json_file} não foi encontrado.")
    except Exception as e:
        raise Exception(f"Erro ao processar os dados do arquivo JSON: {e}")


def main():
    print("Esta é a questão: Análise com Pandas")
    arquivo_json = "INFwebNet.json"

    media = calcular_media_idade(DATA_PATH + arquivo_json)
    print(f"A média de idade dos INFNETianos é: {media:.2f} anos")