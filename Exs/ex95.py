dados = {}
gol = []
cont = 0
dados['nome'] = str(input('Nome do jogador: '))
dados['npartida'] = int(input('N° de partidas: '))
while cont <= (dados['npartida'] - 1):
    gol.append(int(input(f'  Quantos gols no {cont+1}° jogo: ')))
    cont += 1
dados['gol'] = gol[:]
dados['total'] = sum(dados['gol'])
print('=-'*30)
print(f'{dados}')
print('=-'*30)
for i, v in dados.items():
    print(f'O campo {i} tem o valor {v}')
print('=-'*30)
print(f'O jogador {dados["nome"]} jogou {dados["npartida"]} partidas.')
for i, v in enumerate(dados['gol']):
    print(f'{i} {v}')