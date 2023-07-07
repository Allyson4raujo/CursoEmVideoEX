import random
cont = 0
while True:
    jogada = 'P', 'I'
    jogadacomp = random.randint(0, 10)
    print('=' * 25)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=' * 25)
    valor = int(input('Digite um valor: '))
    jogada = str(input('Par ou Ímpar: '))[0].upper().strip()
    print('=' * 25)
    resultado = valor + jogadacomp
    print(f'Você jogou {valor} o computador jogou {jogadacomp}. Total de {resultado}')
    if jogada == 'P':
        if resultado % 2 == 0:
            cont += 1
            print('\033[1;32mVocê venceu !\033[m deu PAR')
            print('Vamos jogar novamente ..')
        else:
            print('\033[1;31mVocê perdeu!\033[m deu Impar')
            break
    elif jogada == 'I':
        if resultado % 2 != 0:
            cont += 1
            print('\033[1; 32mVocê venceu !\033[m deu Impar')
            print('Vamos jogar novamente .. ')
        else:
            print('\033[1;31mVocê perdeu!\033[m deu PAR')
            break
print('GAME OVER!! você venceu \033[1;32m{}\033[m vezes.'.format(cont))