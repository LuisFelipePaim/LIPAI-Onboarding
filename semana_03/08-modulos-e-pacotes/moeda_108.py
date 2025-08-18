import moeda

valor = float(input('Digite o preço: '))
aumento = float(input('Digite o aumento: '))
reducao = float(input('Digite a redução: '))

valor_dobrado = moeda.dobro(valor)
valor_metade = moeda.metade(valor)
valor_aumentado = moeda.aumentar(valor, aumento)
valor_reduzido = moeda.diminuir(valor, reducao)

print(f'A metade de {moeda.moeda(valor)} é igual a: {moeda.moeda(valor_metade)}')
print(f'O dobro de {moeda.moeda(valor)} é igual a: {moeda.moeda(valor_dobrado)}')
print(f'{moeda.moeda(valor)} aumentado {aumento}% é igual a: {moeda.moeda(valor_aumentado)}')
print(f'{moeda.moeda(valor)} diminuido {reducao}% é igual a: {moeda.moeda(valor_reduzido)}')
