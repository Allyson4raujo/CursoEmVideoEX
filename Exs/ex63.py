# screva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência
# de Fibonacci. Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8
print('== Sequencia de Fibonacci ==')
n1 = 0
n2 = 1
cont = 2
n = int(input('Quantos termos você quer monstrar ? '))
print(f'\033[1;34m{n1}\033[m - \033[1;34m{n2}\033[m - ', end='')
while cont < n:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(f'{n3} - ', end='')
    cont+=1
print('\033[1;34mFIM')
