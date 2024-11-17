import json
import pandas as pd


def carregar_dados(arquivo_json):
    """
    Carrega os dados de um arquivo JSON.

    Args:
        arquivo_json (str): Caminho do arquivo JSON.

    Returns:
        list: Lista de dados carregados.
    """
    try:
        with open(arquivo_json, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except Exception as e:
        raise Exception(f"Erro ao carregar o arquivo JSON: {e}")

def salvar_dados(arquivo_json, dados):
    """
    Salva os dados no arquivo JSON.

    Args:
        arquivo_json (str): Caminho do arquivo JSON.
        dados (list): Dados a serem salvos.
    """
    try:
        with open(arquivo_json, 'w', encoding='utf-8') as file:
            json.dump(dados, file, indent=4, ensure_ascii=False)
    except Exception as e:
        raise Exception(f"Erro ao salvar os dados no arquivo JSON: {e}")
    


def pd_carregar_dados(arquivo_json):
    """
    Carrega os dados de um arquivo JSON em um DataFrame.

    Args:
        arquivo_json (str): Caminho do arquivo JSON.

    Returns:
        pd.DataFrame: DataFrame com os dados carregados.
    """
    try:
        with open(arquivo_json, 'r', encoding='utf-8') as file:
            dados = json.load(file)
        return pd.DataFrame(dados)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Nome", "Idade", "Cidade", "Estado", "Hobbys", "Coding", "Jogos"])
    except Exception as e:
        raise Exception(f"Erro ao carregar o arquivo JSON: {e}")

def pd_salvar_dados(arquivo_json, dataframe):
    """
    Salva os dados de um DataFrame em um arquivo JSON.

    Args:
        arquivo_json (str): Caminho do arquivo JSON.
        dataframe (pd.DataFrame): DataFrame com os dados a serem salvos.
    """
    try:
        dataframe.to_json(arquivo_json, orient="records", indent=4, force_ascii=False)
    except Exception as e:
        raise Exception(f"Erro ao salvar os dados no arquivo JSON: {e}")
    