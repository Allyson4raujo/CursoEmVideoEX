print('== Gerador de PA ==')
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
cont = 0
mais = 10
while mais != 0:
    total = cont + mais
    while cont < total:
        print(f'{p} -> ', end='')
        p += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos quer monstrar a mais ? '))
print(f'Foram monstrados {cont} termos')
print('FIM')