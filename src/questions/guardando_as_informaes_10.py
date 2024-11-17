from src.questions.completando_os_dados_9 import unificar_e_completar_infos
from src.helpers.json_utils import pd_salvar_dados

# 10 - Guardando as Informações
########################

def main():
    print("Esta é a questão: Guardando as Informações")
    
    arquivo_json_saida = "src/data/INFwebNet_Data.json"
    try:
        arquivo_json = "src/data/INFwebNet.json"
        arquivo_csv = "src/data/INFwebNet.csv"
        arquivo_txt = "src/data/dados_usuarios_novos.txt"

        df = unificar_e_completar_infos(arquivo_json, arquivo_csv, arquivo_txt)

        pd_salvar_dados(arquivo_json_saida, df)
    except Exception as e:
        print(e)
    finally:
        print("Base de dados atualizada com sucesso em:", arquivo_json_saida)