#  solicite ao usuário 3 notas e apresente o resultado da média aritmética das notas

nota_1 = float(input('\nDigite a primeira nota: '));
nota_2 = float(input('\nDigite a segunda nota: '));
nota_3 = float(input('\nDigite a terceira nota: '));

media = round((nota_1 + nota_2 + nota_3)/3, 2)

print(f'Média das notas: {media}')