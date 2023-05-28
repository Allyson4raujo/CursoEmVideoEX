import random
cont = 0
nomes = []
while True:
    cont += 1
    if cont != 5:
        aluno = input(f'{cont}° Aluno: ')
        nomes.append(aluno)
    else:
        break
nomes_original = nomes[:]
random.shuffle(nomes)
for i, nome in enumerate(nomes):
    print(f'{i+1}° A se apresentar: {nome}')




