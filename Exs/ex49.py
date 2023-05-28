#TABUADA USANDO FOR
n = int(input('Digite um número para ver a tabuada: '))
while True:
    for c in range(1, 11):
        mult = n * c
        print(f'{n} x {c} = {mult:2}')
    escolha = str(input('Deseja continuar   [S/N] ?  ')).strip().upper()
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar   [S/N] ?  ')).strip().upper()
    if escolha ==  'S':
        n = int(input('Digite um número para ver a tabuada: '))
    else:
        break
print('Fim do programa.')

