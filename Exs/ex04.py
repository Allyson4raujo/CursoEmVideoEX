'''Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
informações possíveis sobre ele.'''

var = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(var))
print('Só tem espaços ? ', var.isspace())
print('É um número ?', var.isnumeric())
print('É alfabetico ? ', var.isalpha())
print('É alfanumerico ? ', var.isalnum())
print('Esta em minuscula ?', var.islower())
print('Esta em maiuscula ?', var.isupper())
print('Está capitalizada ?', var.istitle())
