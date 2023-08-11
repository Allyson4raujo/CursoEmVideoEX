cadastro = []
cadastroTemp = []
cont = 0
maior = menor = 0
while True:
    cadastroTemp.append(str(input('Nome: ')))
    cadastroTemp.append(float(input('Peso: ')))
    if cont == 0:
        maior = menor = cadastroTemp[1]
    else:
        if cadastroTemp[1] > maior:
            maior = cadastroTemp[1]
        if cadastroTemp[1] < menor:
            menor = cadastroTemp[1]
    cadastro.append(cadastroTemp[:])
    cadastroTemp.clear()
    esc = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    cont += 1
    while esc not in 'SN':
        print('Opção inválida. Tente novamente.')
        esc = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if esc == 'N':
        break
print(f'Pessoas cadastradas: {cadastro}')
print(f'\nTotal de pessoas cadastradas: \033[1;31m{cont}\033[m')
print(f'Maior Peso: \033[1;31m{maior}Kg\033[m', end='')
for p in (cadastro):
    if p[1] == maior:
        print(f' \033[1;31m{p[0]}\033[m', end='')
print(f'\nMenor Peso: \033[1;31mKg{menor}\033[m', end='')
for p in (cadastro):
    if p[1] == menor:
        print(f' \033[1;31m{p[0]}\033[m', end='')

