#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
alunos = []

for c in range(0, 4):
    aluno = (input(f'Digite o nome do {c+1}° aluno: '))
    alunos.append(aluno)

sorteio = choice(alunos)
print(f'O aluno sorteado foi {sorteio}')

'''
                            L5 Criei uma lista vazia.
                            L7 Criei uma repetição que vai acontecer 4 vezes.
                            L8 criei uma variavel (aluno) ela vai armazenar o nome que o usuario digitar
                            L9 A lista vazia chamada (alunos) vai receber o nome que for digitado na variavel (aluno)
                            L11 Fiz o sorteio da lista (alunos) usando a função choice
'''