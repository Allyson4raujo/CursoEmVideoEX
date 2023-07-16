v1 = int(input('Digite um número: '))
v2 = int(*input('Digite outro número: '))
v3 = int(input('Digite mais um número: '))
v4 = int(input('Digite o último número: '))
valores = (v1, v2, v3, v4)
print('\nO valor 9 apareceu {} vezes.'.format(valores.count(9)))
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)}º posição.')
elif not 3 in valores:
    print('Não aparceu o valor 3 valor na tupla.')
cont = 0
par = []
for c in valores:
    if c % 2 == 0:
        par.append(c)
        cont += 1
if len(par) > 0:
    print(f'Os valores PAR foram: {par} total de {cont}')
else:
    print('Não tivemos PAR')
print('UFA terminei ')