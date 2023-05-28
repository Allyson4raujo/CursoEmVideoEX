import random
import time
from random import choice
from time import sleep

print('\033[1;34mJOGO DO PEDRA, PAPEL E TESOURA !\033[m')
opcoes = ('PEDRA', 'PAPEL', 'TESOURA')
jogadapc = random.choice(opcoes)
for i, v in enumerate(opcoes):
    print(f'[{i}] \033[1;34m{v}\033[m')
jogada = int(input('Qual a sua jogada ? '))
while jogada not in (0,1,2):
    print('Escolha inválida. Tente novamente')
    jogada = int(input('Qual a sua jogada ? '))
time.sleep(0.3)
print('\033[1;34mJO')
time.sleep(0.3)
print('KEN')
time.sleep(0.3)
print('PO!!\033[m')
print('=-'*12)
print(f'\033[1;35mComputador jogou {jogadapc}\033[m\n\033[1;34mJogador jogou {opcoes[jogada]}\033[m')
print('=-'*11)
if jogadapc == opcoes[jogada]:
    print('\033[1;33mEMPATE!')
else:
    if opcoes[jogada] == opcoes[0] and jogadapc == opcoes[2] or opcoes[jogada] == opcoes[1] and jogadapc == opcoes[0] \
            or opcoes[jogada] == opcoes[2] and jogadapc == opcoes[1]:
        print('\033[1;32mJOGADOR VENCEU!\033[m')
    else:
        print('\033[1;31mJOGADOR PERDEU!\033[m')

