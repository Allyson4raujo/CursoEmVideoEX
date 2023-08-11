from random import randint
from operator import itemgetter
c = 1
jogo = {}
ranking = ()
while c <=5:
    jogada = randint(1, 6)
    jogo[f'jogador{c}'] = f'{jogada}'
    c+=1
for i, v in jogo.items():
    print(f'O {i} tirou {v} nos dados.')
print('='*30)
print(f'{"== RANKING DOS JOGADORES ==":^30}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for j, v in enumerate(ranking):
    print(f'{j+1}° lugar: {v[0]} tirou {v[1]}')




