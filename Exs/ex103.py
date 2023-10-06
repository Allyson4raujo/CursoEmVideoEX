def ficha(nome='desconhecido', gol=0):
    return f'O jogador {nome} fez {gol} gol(s) no campeonato.'

#Programa principal
nome = str(input('Nome do jogador: ').strip())
gol = input('Número de gol(s): ')
if nome == '':
    nome = '<Desconhecido>'
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

print(ficha(nome, gol))
