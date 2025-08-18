numeros = input('Digite os numeros(formato: n1, n2, n3): ')
numero_l = numeros.split(',')

maior = menor = numero_l[0]
for numero in numero_l:
    if(float(numero) < float(menor)):
        menor = float(numero)
    if(float(numero) > float(maior)):
        maior = float(numero)

print(f'maior número: {maior}')
print(f'menor número: {menor}')        