valores = []
impar = []
par = []
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    escolha = str(input('Deseja continuar ? [S/N] ')).strip().upper()
    if escolha in 'N':
        break
print('\nA lista completa {}'.format(valores))
print(f'A lista de pares {par}')
print(f'A lista de impar {impar}')
