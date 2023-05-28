cont = soma = 0

for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        cont += 1
        soma += n

print(f'A soma dos números pares {soma}.\nAo total foram {cont} números pares.')


