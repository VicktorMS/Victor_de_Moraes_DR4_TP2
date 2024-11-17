from helpers.json_utils import carregar_dados, salvar_dados
from utils.constants import DATA_PATH

# 3 - Cadastro Simplificado
########################

def cadastrar_infnetiano(arquivo_json):
    """
    Permite ao usuário cadastrar um novo INFNETiano.

    Args:
        arquivo_json (str): Caminho do arquivo JSON.
    """
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")

    novo_infnetiano = {
        "Nome": nome,
        "Idade": idade,
        "Cidade": cidade,
        "Estado": estado,
        "Amigos": ""
    }

    dados = carregar_dados(arquivo_json)
    dados.append(novo_infnetiano)
    salvar_dados(arquivo_json, dados)
    print(f"INFNETiano {nome} cadastrado com sucesso!")


def main():
    print("Esta é a questão: Cadastro Simplificado")
    cadastrar_infnetiano(DATA_PATH + 'INFwebNet.json')