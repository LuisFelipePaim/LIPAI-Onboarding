
def carregar_dados_alunos(nome_arquivo ):
    arquivo = open(nome_arquivo, 'r')
    for linha in arquivo:
        linha_list = linha.split(',')
              
        linha_tupla = [str(lin.strip()) for lin in linha_list]
        print(linha_tupla)

    arquivo.close()

carregar_dados_alunos('dados.txt')