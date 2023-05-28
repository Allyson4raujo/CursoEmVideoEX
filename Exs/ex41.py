#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:

from datetime import date

def categoria(idade):
    if idade <= 9:
        return 'MIRIM'
    elif idade <= 14:
        return 'INFANTIL'
    elif idade <= 19:
        return 'JÚNIOR'
    elif idade <= 25:
        return 'SÊNIOR'
    else:
        return 'MASTER'

atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print(f'O atleta tem {idade}')
print(f'Classificação: {categoria(idade)}')



