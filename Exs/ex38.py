#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- Não existe valor maior, os dois são iguais

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('\033[1;36mO primeiro número é maior.')
elif n2 > n1:
    print('\033[1;35mO segundo número é maior.')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais.')
