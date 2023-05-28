#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

print('TIRANDO IMC')
peso = int(input('Digite seu peso: (Kg) '))
altura = float(input('Digite sua altura: (m) '))
def calcularImc(peso, altura):
    imc = peso / (altura * altura)
    if imc < 18.5:
        resultado = 'Abaixo do peso.'
    elif imc > 18.5 and imc < 25:
        resultado = 'Peso ideial'
    elif imc >= 25 and imc < 30:
        resultado = 'Sobrepeso'
    elif imc >= 30 and imc <= 40:
        resultado = 'Obesidade'
    else:
        resultado = 'Obesidade morbida'

    return imc, resultado



valor = calcularImc(peso, altura)
imc, resultado = valor
print('O IMC dessa pessoa {:.1f}'.format(imc))
print('resultado: {}'.format(resultado))
