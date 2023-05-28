#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
from time import sleep
while True:
    n = int(input('Digite um número entre 0 e 9999: '))
    print(f'Analizando o número {n}', end='')
    print('.', end='')
    sleep(0.3)
    print('.', end='')
    sleep(0.3)
    print('.')
    if 0 <= n <= 9999:
        break
    else:
        print('Número inválido. Tente novamente.')
print(f'Unidade: {n // 1 % 10}')
print(f'Dezena: {n // 10 % 10}')
print(f'Centena: {n // 100 % 10}')
print(f'Milhar: {n // 1000 % 10}')
