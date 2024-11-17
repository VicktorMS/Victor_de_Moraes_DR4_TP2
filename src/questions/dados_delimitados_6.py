# 6 - Dados Delimitados
########################
import csv

def ler_usuarios_delimitados(arquivo_txt):
    """
    Lê um arquivo delimitado por ponto e vírgula (;) e retorna os dados em formato de lista de dicionários.

    Args:
        arquivo_txt (str): Caminho do arquivo de entrada.

    Returns:
        list[dict]: Lista de dicionários com os dados dos usuários.
    """
    try:
        with open(arquivo_txt, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            dados = [linha for linha in reader]
        return dados
    except FileNotFoundError:
        raise FileNotFoundError(f"O arquivo {arquivo_txt} não foi encontrado.")
    except Exception as e:
        raise Exception(f"Erro ao ler o arquivo delimitado: {e}")


def main():
    print("Esta é a questão: Dados Delimitados")
    arquivo_txt = "src/data/dados_usuarios_novos.txt"
    try:
        dados = ler_usuarios_delimitados(arquivo_txt)
        print(f"Total de usuários lidos: {len(dados)}")
        print("Exemplo de usuário lido:")
        print(dados[0])  
    except Exception as e:
        print(e)