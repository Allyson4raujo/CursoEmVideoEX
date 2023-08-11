matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = somat = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para matriz [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
print('-'*22)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-'*22)
print(f'Soma par = {somap}')
for l in range(0, 3):
    somat += matriz[l][2]
print(f'Soma da 3° coluna = {somat}')
print(f'Maior valor da segunda linha = {max(matriz[1])}')
