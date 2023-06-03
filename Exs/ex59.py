n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while True:
    print('[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Maior\n'
          '[4] Novos números\n'
          '[5] Sair do programa')
    escolha = int(input('Qual sua escolha: '))
    if escolha == 1:
        print(f'\033[31mA soma é {n1+n2}\033[m')
    elif escolha == 2:
        print(f'\033[31mA multiplicação é {n1*n2}.\033[m')
    elif escolha == 3:
        if n1 > n2:
            print(f'\033[31mO maior valor é {n1}.\033[m')
        elif n2 > n1:
            print(f'\033[31mO maior valor é {n2}.\033[m')
        else:
            print('\033[31mOs dois valores são iguais.\033[m')
    elif escolha == 4:
        print('Informe os valores novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif escolha == 5:
        print('\033[31mEncerrando programa.')
        break
    else:
        print('Opção invalida. tente novamente..')
print('FIM')