#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor.
maior = menor = 0
for c in range(0, 5):
    peso = float(input(f'Peso da {c+1}° pessoa: '))
    if c == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior}\nO menor peso lido foi {menor}')
