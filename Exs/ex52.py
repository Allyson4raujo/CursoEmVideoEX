#  Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
cont = 0
num = int(input('Digite um número: '))
for c in range(1, num+1):
    if num % c == 0:
        cont += 1
        print(f'\033[1;37m{c}\033[m', end=' ')
    else:
        print(f'\033[1;31m{c}\033[m', end=' ')
if cont == 2:
    print('\n\033[1;34mNúmero PRIMO!\033[m')
else:
    print(f'\n\033[1;31mNúmero não PRIMO!\033[m')
print(f'O n° foi dividido \033[1;37m{cont}\033[m vezes.')

