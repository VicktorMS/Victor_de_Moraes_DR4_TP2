import pandas as pd
from helpers.json_utils import pd_carregar_dados, pd_salvar_dados
from utils.constants import DATA_PATH
# 5 - Ampliando as Informações
########################

def cadastrar_infnetiano_completo(arquivo_json):
    """
    Permite ao usuário cadastrar um novo INFNETiano com campos adicionais.

    Args:
        arquivo_json (str): Caminho do arquivo JSON.
    """
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")

    hobbys = input("Digite os hobbys separados por vírgula: ").split(',')
    coding = input("Digite as linguagens de programação separadas por vírgula: ").split(',')

    jogos = []
    while True:
        jogo = input("Digite o nome de um jogo (ou pressione Enter para finalizar): ")
        if not jogo:
            break
        plataforma = input(f"Digite a plataforma onde {jogo} foi jogado: ")
        jogos.append({"jogo": jogo, "plataforma": plataforma})

    novo_infnetiano = {
        "Nome": nome,
        "Idade": idade,
        "Cidade": cidade,
        "Estado": estado,
        "Amigos": "",
        "Hobbys": [h.strip() for h in hobbys if h.strip()],
        "Coding": [c.strip() for c in coding if c.strip()],
        "Jogos": jogos
    }

    df = pd_carregar_dados(arquivo_json)
    df = pd.concat([df, pd.DataFrame([novo_infnetiano])], ignore_index=True)
    pd_salvar_dados(arquivo_json, df)

    print(f"INFNETiano {nome} cadastrado com sucesso!")

def main():
    print("Esta é a questão: Ampliando as Informações")
    
    cadastrar_infnetiano_completo(DATA_PATH + 'INFwebNet.json')