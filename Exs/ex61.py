print(f'== Gerador de PA ==')
print('-'*20)
p = int(input('\033[;31mPrimeiro termo: \033[m'))
r = int(input('\033[;34mRazão: \033[m'))
print(f'\033[1;31m{p}\033[m'' -> ', end='' )
cont = 0

while cont < 10:
    p += r
    print(f'\033[;34m{p}\033[m -> ', end='')
    cont+= 1
print('\033[1;31mFIM!\033[m')