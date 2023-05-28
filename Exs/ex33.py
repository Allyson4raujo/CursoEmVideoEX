# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
maior = menor = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    if c == 0:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(f'\nMaior {maior}')
print(f'Menor {menor}')