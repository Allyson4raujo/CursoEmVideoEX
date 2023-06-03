from random import randint
from time import sleep
cont = 0
comp = randint(1, 10)
print('Sou seu computador...\nAcabei de pensar em um número entre \033[1;31m0\033[m e \033[1;31m10\033[m.\nSerá que você'
    ' consegue ' 'adivinhar ?')
print('. ', end='')
sleep(0.3)
print('. ', end='')
sleep(0.3)
print('. ', end='')
sleep(0.3)
print()
while True:
    escolha = int(input('Qual o seu palpite ? '))
    cont += 1
    if escolha > comp:
        print('\033[1;31mMenos... Tente mais uma vez\033[m')
    elif escolha < comp:
        print('\033[1;34mMais... tente mais uma vez\033[m')
    elif escolha == comp:
        print(f'\033[1;32mVocê acertou com {cont} tentativas. Parabéns!!\033[m')
        break
