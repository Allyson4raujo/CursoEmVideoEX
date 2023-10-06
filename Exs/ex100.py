from random import randint
numeros = []

def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        numeros.append(randint(1, 10))
    print(f'{numeros} pronto!')

def somapar():
    soma = tot = 0
    print(f'Somando os valores pares de {numeros}, temos', end='')
    for c in numeros:
        if c % 2 == 0:
            soma += c
            tot = soma
    print(f' {tot}')

sorteia()
somapar()