def aumentar(n, taxa=0, f=False):
    r = n + (n * taxa/100)
    if f is False:
        return r
    else:
        return real(n)


def diminuir(n, taxa=0, f=False):
    r = n - (n * taxa/100)
    return r if f is False else real(n)


def dobro(n=0, f=False):
    r = n * 2
    return r if not f else real(n)

def metade(n=0, f=False):
    r = n / 2
    return r if not f else real(n)

def real(valor=0):
    return f'R${valor:.2f}'.replace('.', ',')