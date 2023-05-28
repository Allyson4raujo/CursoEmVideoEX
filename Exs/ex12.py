# Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = float(input('Digite o valor do produto: '))
nvalor = valor - (valor * 5 /100)
print(f'O produto que custava {valor}, na promoção com desconto de 5% vai custar {nvalor:.2f}')

