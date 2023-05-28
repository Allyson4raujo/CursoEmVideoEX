#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
#descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu
def tracado():
    print('\033[1;31m=-\033[m' * 20)


from random import randint
from time import sleep
tracado()
print('Vou pensar em um número entre 0 e 5. Tente adivinhar..')
tracado(),
comp = randint(0, 5)
usu = int(input('Em qual número eu pensei ? '))
print('Processando...')
sleep(0.5)
if comp == usu:
    print(f'Parabéns! eu pensei no número {comp} e você acertou xD')
else:
    print(f'GANHEI! Eu pensei no número {comp} e não no {usu}\nTENTE NOVAMENTE..!')
