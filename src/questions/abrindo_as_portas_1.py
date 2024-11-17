import csv
from utils.constants import DATA_PATH
# 1 - Abrindo as Portas
########################

def processar_arquivo(input_file='rede_INFNET.txt', output_file='INFwebNet.csv'):
    """
    Processa um arquivo de texto e exporta os dados para um arquivo CSV.

    Args:
        input_file (str): Caminho do arquivo de entrada.
        output_file (str): Caminho do arquivo de saída em formato CSV.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"O arquivo {input_file} não foi encontrado.")
    except Exception as e:
        raise Exception(f"Erro ao abrir o arquivo {input_file}: {e}")

    dados_processados = []
    try:
        for line in lines:
            campos = line.strip().split('?')
            if len(campos) >= 4:
                nome, idade, cidade, estado, *amigos = campos
                amigos = ', '.join(amigos)
                dados_processados.append([nome, idade, cidade, estado, amigos])
    except Exception as e:
        raise Exception(f"Erro ao processar os dados do arquivo: {e}")

    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Nome", "Idade", "Cidade", "Estado", "Amigos"])
            writer.writerows(dados_processados)
    except Exception as e:
        raise Exception(f"Erro ao salvar o arquivo {output_file}: {e}")



def main():
    print("Esta é a questão: Abrindo as Portas")
    input_file = DATA_PATH + 'rede_INFNET.txt'
    output_file = DATA_PATH + 'INFwebNet.csv'
    processar_arquivo(input_file, output_file)
    print(f"Arquivo {output_file} gerado com suceso!")
