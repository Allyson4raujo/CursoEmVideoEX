
def ajuda(com):
    help(com)

def tit(msg, cor=0):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)



#Programa principal
comando = ''
while True:
    tit('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)