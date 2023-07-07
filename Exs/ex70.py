totvalor = mil = maiorv = menorv = cont = 0
escolha = ' '
maiornome = menornome = ' '
while True:
    n = str(input('Nome do produto: '))
    v = float(input('Preço do produto R$: '))
    escolha = str(input('Deseja continuar ?[S/N] ')).strip().upper()[0]
    if escolha not in 'SN':
        escolha = str(input('Deseja continuar ? ')).strip().upper()[0]
    totvalor += v
    if cont == 0:
        maiorv = menorv = v
        maiornome = menornome = n
    else:
        if v > maiorv:
            maiorv = v
            maiornome = n
        if v < menorv:
            menorv = v
            menornome = n
    if v > 1000:
        mil += 1
    cont += 1
    if escolha in 'N':
        break
print(f'\ntotal valor produtos: {totvalor}\n Total n° de produtos {cont}')
print(f'Temos {mil} produtos custando + de R$1.000')
print(f'O produto mais cara foi {maiornome} custando: R${maiorv}')
print(f'O produto mais cara foi {menornome} custando: R${menorv}')
