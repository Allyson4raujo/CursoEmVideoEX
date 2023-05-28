#Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

from time import sleep
n = int(input('Digite um valor: '))
print(f'Analizando valor... ')
sleep(0.5)
print(f'O antecessor do valor {n} é {n-1}.\nO sucessor do valor {n} é {n+1} ')
