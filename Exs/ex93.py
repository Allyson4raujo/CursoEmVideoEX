dados = {}
dadosf = {}
cont = 0
dados['nome'] = str(input('Nome do jogador: '))
dados['npartida'] = int(input('Número de partidas: '))
gol = []
while cont <= (dados['npartida'] - 1):
    gol.append(int(input(f'Quantos gols no {cont+1}° jogo: ')))
    cont += 1
dados['gols'] = gol[:]
print('=-'*30)
print(dados)
print('=-'*30)
dadosf = {'nome': dados['nome'], 'gols': dados['gols'], 'total': sum(dados['gols'])}
for i, v in dadosf.items():
    print(f'O campo {i} tem o valor {v}')
print('=-'*30)
dadosn = {'nome': dados['nome'], 'npartida': dados['npartida']}
print(f'O jogador {dados["nome"]} jogou {dados["npartida"]} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'  => Na {i+1}partida {i+1}, fez {v} gols')

