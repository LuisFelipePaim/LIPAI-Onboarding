def carregar_dados_alunos(nome_arquivo ):
    arquivo = open(nome_arquivo, 'r')
    for linha in arquivo:
        linha_list = linha.split(',')
              
        linha_tupla = [str(lin.strip()) for lin in linha_list]
        print(linha_tupla)

    arquivo.close()

carregar_dados_alunos('dados.txt')

def linha_para_dict(tupla_arquivos, lista_chaves):
    valores = tupla_arquivos.strip().split(',')

    dicionario_resultado = {}

    contador = 0
    while contador < len(lista_chaves):
        chave_atual = lista_chaves[contador]
        valor_atual = valores[contador]
        dicionario_resultado[chave_atual] = valor_atual
        contador += 1


    return dicionario_resultado
 