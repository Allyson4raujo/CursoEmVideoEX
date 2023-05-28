#Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite um valor para ver a tabuada: '))
for c in range(0, 11):
    v = n*c
    print(f'{n:2} x {c} = {v:2}')
