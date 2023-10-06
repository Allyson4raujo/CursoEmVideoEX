def leiaint(num):
    while True:
        num = input('Digite um número: ')
        if num.isnumeric():
            return int(num)
        else:
            print('\033[1;31mERROR. Digite um valor númerico válido.\033[m')


#Programa principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')