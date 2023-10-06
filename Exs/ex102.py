def fatorial(n, show=False):
    f = 1
    c = 1
    while c <= n:
        if show:
            print(f'{c}', end='')
            if c < n:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
        c += 1
    return f

n = int(input('Calculo de fatorial. Digite o número: '))
print(fatorial(n, show=True))
