def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    if i < f:
        c = i
        while c <= f:
            print(f'{c} ', end='')
            c += p
    else:
        c = i
        while c >= f:
            print(f'{c} ', end='')
            c -= p
    print()

# Contagem de 1 até 10, de 1 em 1
contador(1, 10, 1)

# Contagem de 10 até 0, de 2 em 2
contador(10, 0, 2)

#programa principal
contador(1, 10, 1)
contador(10, 0, 5)