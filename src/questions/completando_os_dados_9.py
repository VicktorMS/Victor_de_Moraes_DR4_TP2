from src.questions.criando_informaes_8 import unificar_e_criar_infos

# 9 - Completando os Dados
########################

def preencher_valores_ausentes(df):
    """
    Preenche valores ausentes em duas colunas do DataFrame com critérios definidos.

    Args:
        df (pd.DataFrame): DataFrame com valores ausentes.

    Returns:
        pd.DataFrame: DataFrame atualizado com valores preenchidos.
    """
    try:
        # Preenche valores ausentes na coluna "Idade" com a média das idades (arredondada para inteiro)
        if 'Idade' in df.columns:
            media_idade = df['Idade'].mean()
            df['Idade'] = df['Idade'].fillna(round(media_idade))

        # Preenche valores ausentes na coluna "Estado" com 'Rio de janeiro'
        if 'estado' in df.columns:
            df['estado'] = df['estado'].fillna('Rio de janeiro')

        return df
    except Exception as e:
        raise Exception(f"Erro ao preencher valores ausentes: {e}")

def unificar_e_completar_infos(dados_json, dados_csv, dados_txt):
    """
    Unifica dados de diferentes fontes, adiciona a coluna 'ano_nascimento' e preenche valores ausentes.

    Args:
        dados_json (str): Caminho do arquivo JSON.
        dados_csv (str): Caminho do arquivo CSV.
        dados_txt (str): Caminho do arquivo TXT delimitado por ponto e vírgula (;).

    Returns:
        pd.DataFrame: DataFrame atualizado com dados preenchidos para Idade e Estado.
    """
    try:
        # Unifica todos os dados e adiciona a coluna 'ano_nascimento'
        df = unificar_e_criar_infos(dados_json, dados_csv, dados_txt)

        # Preenche Valores nulos de idade e estado
        df = preencher_valores_ausentes(df)

        return df
    except Exception as e:
        raise Exception(f"Erro ao consolidar e completar dados: {e}")

def main():
    print("Esta é a questão: Completando os Dados")
    # Caminhos das bases de dados
    arquivo_json = "src/data/INFwebNet.json"
    arquivo_csv = "src/data/INFwebNet.csv"
    arquivo_txt = "src/data/dados_usuarios_novos.txt"

    try:
        df = unificar_e_completar_infos(arquivo_json, arquivo_csv, arquivo_txt)

        print(f"DataFrame Atualizado - Total de registros: {len(df)}")
        print(df.head())  # Exibe os primeiros registros como exemplo
    except Exception as e:
        print(e)