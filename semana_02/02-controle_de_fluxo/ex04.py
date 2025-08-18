identificador = input('Digite o identificador: ')
if len(identificador) == 7:
    if identificador[0] == 'B' and identificador[1] == 'R':
        if identificador[2:6].isdigit():
            if identificador[-1] == 'X':
                print('O código é válido!')
            else:
                print('Código inválido! O código não termina com caracter X!')
        else: 
            print('Código inválido! Código não possui quatro números naturais!')           
        
    else:
        print("Código inválido! Código não inicia com os caracteres BR")
else:
    print('Código inválido! Código possui mais do que sete caracteres!')       

        



