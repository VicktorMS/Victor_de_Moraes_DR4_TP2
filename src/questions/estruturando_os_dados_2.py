import csv
import json
from utils.constants import DATA_PATH
# 2 - Estruturando os Dados
########################

def csv_para_json(input_csv, output_json):
    """
    Converte os dados de um arquivo CSV para um arquivo JSON estruturado.

    Args:
        input_csv (str): Caminho do arquivo CSV de entrada.
        output_json (str): Caminho do arquivo JSON de saída.
    """
    try:
        with open(input_csv, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            dados = [linha for linha in reader]
    except FileNotFoundError:
        raise FileNotFoundError(f"O arquivo {input_csv} não foi encontrado.")
    except Exception as e:
        raise Exception(f"Erro ao ler o arquivo CSV: {e}")
    
    try:
        with open(output_json, 'w', encoding='utf-8') as jsonfile:
            json.dump(dados, jsonfile, indent=4, ensure_ascii=False)
    except Exception as e:
        raise Exception(f"Erro ao salvar o arquivo JSON: {e}")

def main():
    print("Esta é a questão: Estruturando os Dados")
    input_file = "INFwebNet.csv"
    output_file = "INFwebNet.json"
    csv_para_json(DATA_PATH + input_file, DATA_PATH + output_file)
    print(f"Arquivo {output_file} criado em {DATA_PATH}")
        