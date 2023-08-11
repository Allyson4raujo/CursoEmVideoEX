from random import randint
print('-'*30)
print('JOGOS DA MEGA SENA'.center(30))
print('-'*30)
lista = []
jogos = []
tot = 0
njogadas = int(input('Quantos jogos você quer sortear ? '))
while tot < njogadas:

    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
        if len(lista) == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
print('-'*30)
print('-=-=-=', 'SORTEANDO JOGOS', '-=-=-=')
for i, v in enumerate(jogos):
    print(f'Jogo {i+1}: {v}')