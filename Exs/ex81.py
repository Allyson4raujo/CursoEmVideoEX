valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    escolha = str(input('Deseja continuar ? [S/N]')).upper().strip()
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar ? [S/N]')).upper().strip()
    if escolha in 'N':
        break
print(f'\nVocê digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em forma decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
