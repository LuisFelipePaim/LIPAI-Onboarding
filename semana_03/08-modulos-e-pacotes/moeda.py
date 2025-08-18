def dobro(valor):

    numero_dobro = valor * 2
    return numero_dobro

def metade(valor):
    
    numero_metade = valor / 2
    return numero_metade

def aumentar(valor, porcentagem):

    numero_aumentado = (valor + (valor*(porcentagem/100)))
    return numero_aumentado

def diminuir(valor, porcentagem):
    
    numero_diminuido = (valor - (valor*(porcentagem/100)))
    return numero_diminuido

def moeda(valor):

    valor_str = f"R${str(valor)}"
    return valor_str

    
