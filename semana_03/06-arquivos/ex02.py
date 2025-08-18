def carregar_dados_projeto(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    for linha in arquivo:
        linha_list = linha.split(',')

        linha_tupla = [str(lin.strip()) for lin in linha_list]
        print(linha_tupla)

    arquivo.close()

carregar_dados_projeto('projeto.txt')  