def calcular_volume(comprimento, altura, largura): 
    volume = 0
    volume = (comprimento * altura * largura)/1000
    return volume

def potencia_termostato(volume, temperatura_desejada, temperatura_ambiente):
    potencia = volume * 0.5 * (temperatura_desejada - temperatura_ambiente)
    return potencia

def filtragem_p_hora(volume):
    volume_necessario = volume * 3
    return volume_necessario

comprimento = float(input('Digite o comprimento do aquário: '))
altura = float(input('Digite a altura do aquário: '))
largura = float(input('Digite a largura do aquário: '))
temperatura_desejada = float(input('Digite a temperatura desejada: '))
temperatura_ambiente = float(input('Digite a temperatura ambiente: '))

especificacoes = {
    'comprimento': comprimento,
    'altura': altura,
    'largura': largura,
    'temperatura_desejada': temperatura_desejada,
    'temperatura_ambiente': temperatura_ambiente
}
volume = potencia = volume_necessario = 0
volume = calcular_volume(especificacoes['comprimento'], especificacoes['altura'], especificacoes['largura'])
print(f'O volume do aquário é: {round(volume,2)}')
potencia = potencia_termostato(volume, especificacoes['temperatura_desejada'], especificacoes['temperatura_ambiente'])
print(f'A potencia do termostato necessária é: {round(potencia,2)}')
volume_necessario =filtragem_p_hora(volume)
print(f'O volume de filtragem necessária por hora para o aquário é de: {round(volume_necessario,2)}')
