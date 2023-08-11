valores = [[], []]
for c in range(0, 7):
    valor = int(input(f'Digite o {c+1}° valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
print(f'Os valores pares são {valores[0]}')
print(f'Os valores ímpares são {valores[1]}')