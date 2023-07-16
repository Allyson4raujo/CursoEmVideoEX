times = ('Botafogo', 'Flamengo', 'Palmeiras', 'Corinthians', 'São Paulo', 'Santos', 'Internacional', 'Atlético-MG',
         'Fluminense', 'Grêmio', 'Vasco da Gama', 'Athletico-PR', 'Ceará SC', 'Fortaleza EC', 'Bahia', 'América-MG',
         'Chapecoense', 'Goiás EC', 'Juventude', 'Cuiabá')

print(f'Os 5 \033[1;32mprimeiros\033[m colocados \033[1/32m{times[0:5]}\033[m')
print(f'Os \033[1;31mútimos\033[m 4 colocados \033[1;31m{times[-4:]}\033[m')
print('Os times em ordem alfabética: {}'.format(sorted(times)))
print('O \033[1;34mCorinthias\033[m está na posição \033[1;34m{}º\033[m'.format(times.index("Corinthians")+1))

