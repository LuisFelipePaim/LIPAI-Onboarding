import moeda

valor = float(input('Digite o preço: '))
aumento = float(input('Digite o aumento: '))
reducao = float(input('Digite a redução: '))

valor_dobrado = moeda.dobro(valor)
valor_metade = moeda.metade(valor)
valor_aumentado = moeda.aumentar(valor, aumento)
valor_reduzido = moeda.diminuir(valor, reducao)

print(f'A metade de {valor} é igual a: {valor_metade}')
print(f'O dobro de {valor} é igual a: {valor_dobrado}')
print(f'{valor} aumentado {aumento}% é igual a: {valor_aumentado}')
print(f'{valor} diminuido {reducao}% é igual a: {valor_reduzido}')
