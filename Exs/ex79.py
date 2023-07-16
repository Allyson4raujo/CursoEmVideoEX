valores = []
while True:
    v = (int(input('Digite um valor: ')))
    if v in valores:
        print('\033[1;31mValor duplicado! não posso adicionar\033[m..')
    else:
        print('\033[1;32mValor adicionado a lista\033[m..')
        valores.append(v)
    escolha = str(input('Deseja continuar ? [S/N] ')).upper().strip()[0]
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar ? [S/N] ')).upper().strip()[0]
    if escolha in 'N':
        break
print(f'Os valores na \033[1;34mlista\033[m são: \033[1;34m{sorted(valores)}\033[m')