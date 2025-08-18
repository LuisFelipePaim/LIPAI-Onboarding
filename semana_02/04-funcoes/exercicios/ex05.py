def calcular_imc(individuo): 
    imc = individuo['peso'] / (pow(individuo['altura'], 2))
    return imc
def obter_classificacao(imc):
    if imc < 18.5:
        return 'Baixo peso'
    elif imc >= 18.5 and imc <= 24.9:
        return 'Peso normal'
    elif imc >= 25.0 and imc <= 29.9:
        return 'Excesso de peso'
    elif imc >= 30.0 and imc <= 34.9:
        return 'Obesidade grau I'
    elif imc >= 35.0 and imc <= 39.9:
        return 'Obesidade grau II'
    else:
        return 'Obesidade grau III'
    

    
def situacao_individuo(imc):
    if imc < 18.5:
        return 'Ganhar peso'
    elif imc >= 18.5 and imc <= 24.9:
        return 'Manter peso'
    else:
        return 'Perder peso'
        print('Perder peso')



peso = float(input("Digite seu peso(kg)): "))
altura = float(input("Digite sua altura(m): "))

individuo = {
    'peso': peso,
    'altura': altura
}

imc = calcular_imc(individuo)
print(round(imc, 1))
print(obter_classificacao(imc))
print(situacao_individuo(imc))
