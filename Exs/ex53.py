# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando
# os espaços.

frase = (input('Digite uma frase: ')).upper().strip()
palavra = frase.split()
palavraJunto = ''.join(palavra)
inverso = ''
for letra in range(len(palavraJunto) -1, -1, -1 ):
    print(palavraJunto[letra], end='')
