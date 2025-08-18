identificador = input('Digite o identificador: ')

if len(identificador) == 7 and \
    identificador[0] == 'B' and \
    identificador[1] == 'R' and \
    identificador[2:6].isdigit() and \
    identificador[6] == 'X':
    
    print('O código é válido!')
       
else:
    print("Código inválido!")
        

