# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome completo: ')).upper().strip()
if 'SILVA' in nome:
    print('Seu nome tem silva.')
else:
    print('Seu nome nao tem silva.')