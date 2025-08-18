def faz_soma(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma


numeros = input("Digite os números(formato: n1, n2, n3, ..., nm): ")
numeros_list = numeros.split(',')
numeros_tupla = [int(num.strip()) for num in numeros_list]

resultado = faz_soma(numeros_tupla)
    
print(resultado)

