maior = menor = 0
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f'O maior valor foi {maior} na posição', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f' {i}')
print(f'O menor valor foi {menor} na posição', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f' {i}')
