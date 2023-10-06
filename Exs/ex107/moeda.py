def aumentar(n, taxa):
    r = n + (n * taxa/100)
    return r

def diminuir(n, taxa):
    r = n - (n * taxa/100)
    return r


def dobro(n):
    r = n * 2
    return r

def metade(n):
    r = n / 2
    return r

def real(valor):
    v = float(valor)
    s = f'{v:.2f}'
    s.replace('.', ',')
    return s
