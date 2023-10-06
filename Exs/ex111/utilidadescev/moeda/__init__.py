def aumentar(n, taxa=0, f=False):
    r = n + (n * taxa/100)
    return r if f is False else real(r)



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


def resumo(n, aumento=0, reducao=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analizado: {real(n)}')
    print(f'Dobro do preço: {real(dobro(n))}')
    print(f'Metade do preço: {real(metade(n))}')
    print(f'{aumento}% de aumento: {aumentar(n, aumento, True)} ')
    print(f'{reducao}% de redução: {real(diminuir(n, reducao))} ')
    print('-'*30)
