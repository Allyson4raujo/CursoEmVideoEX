#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
def cor(txt):
    red = '\033[31m'
    reset = '\033[m'
    return f'{red}{txt}{reset}'

n = int(input('\033[1;31mDigite um valor qualquer: \033[m'))
if n % 2 == 0:
    print(cor(f'\nEsse valor {n} é PAR'))
else:
    print(cor('\nEsse valor {} é Ímpar'.format(n)))
