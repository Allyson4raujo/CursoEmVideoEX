from time import sleep
'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

nome = input('Digite seu nome completo: ').strip()
print('Analizando seu nome..')
sleep(0.6)
print(f'Nome com todas as letras minúsculas {nome.lower()}\nNome com todas as letras maiúsculas {nome.upper()}')
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras')
primeiro = nome.split()[0]
print(f'Seu primeiro nome é {primeiro} ele tem {len(primeiro)} letras')