#Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual o maior

def maior(*n):
    maior = cont = 0
    valores = n
    for c in valores:
        if cont == 0:
            maior = c
        else:
            if c > maior:
                maior = c
        cont +=1
    print('Analizando os valores passados..')
    print(f'\033[1;31m{valores}\033[m foram imformados \033[1;31m{len(valores)}\033[m ao todo.')
    print(f'O maior valor foi \033[1;31m{maior}\033[m\n')



maior(3,2,15,13)
maior()

