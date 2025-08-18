def faz_soma(n1, n2, n3):
    soma = n1 + n2 + n3
    print(f'A soma dos números é {soma}')


primeiro_numero = input('Digite o primeiro número: ')
segundo_numero = input('Digite o segundo número: ')
terceiro_numero = input('Digite o terceiro número: ')

n1 = float(primeiro_numero)
n2 = float(segundo_numero)
n3 = float(terceiro_numero)

faz_soma(n1, n2, n3)