# ex01.py crie a função carregar_dados_alunos que recebe como parâmetro
# o nome de um arquivo que contém dados de alunos e retorna uma tupla, 
# onde cada elemento é um dicionário com as 
# seguintes chaves: prontuario, nome e email
# def carregar_dados_alunos(nome_arquivo ):
def carregar_dados_alunos(nome_arquivo ):
    arquivo = open(nome_arquivo, 'r')
    for linha in arquivo:
        linha_list = linha.split(',')
              
        linha_tupla = [str(lin.strip()) for lin in linha_list]
        print(linha_tupla)

    arquivo.close()

carregar_dados_alunos('dados.txt')