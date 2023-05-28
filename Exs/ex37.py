# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
# conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

while True:
    n = int(input('Digite um número: '))
    print('Escolha uma base de conversão:')
    menu = ['Converter em BINÁRIO', 'Converter em OCTAL', 'Converter em HEXADECIMAL', 'Sair']
    for i, v in enumerate(menu):
        print(f'{[i + 1]}{v}')
    escolha = int(input('Sua opção: '))
    if escolha == 1:
        print(f'{n} convertido para BINÁRIO é igual {bin(n)[2:]}')
    elif escolha == 2:
        print(f'{n} convertido para OCTAL é igual {oct(n)[2:]}')
    elif escolha == 3:
        print(f'{n} convertido para HEXADECIMAL é igual {hex(n)[2:]}')
    elif escolha == 4:
        break
