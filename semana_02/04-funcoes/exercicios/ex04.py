def faz_soma(*args):
    soma = 0
    for num in args:
        soma += num

    return soma

entrada = input("Escreva os números: ")
numeros_list_str= entrada.split(',')
numeros_list_float = [float(num) for num in numeros_list_str] 

numeros = faz_soma(*numeros_list_float)

print(numeros)