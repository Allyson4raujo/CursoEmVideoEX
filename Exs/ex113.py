def leiaint(txt):
    while True:
        try:
            n = int(input(txt))
        except (TypeError, ValueError):
            print('\033[31mERROR: Digite um valor inteiro válido\033[m')
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar valor.')
            return 0
        else:
            return n

def leiafloat(txt):
    while True:
        try:
            r = float(input('Digite um valor Real: '))
        except (TypeError, ValueError):
            print('ERROR: Digite um valor REAL')
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar valor.')
            return 0
        else:
            return r



#Programa principal
n = leiaint('Digite um valor Inteiro: ')
r = leiafloat('Digite um valor Real: ')
print(f'Você acabou de digitar os números {n}, {r}')

