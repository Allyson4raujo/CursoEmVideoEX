ex = ('zero', 'um', 'dois', 'três','quatro', 'cinco', 'seis', 'sete', 'oito','nove','dez', 'onze', 'doze', 'treze'
            , 'quatorze','quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Digite um número entre 0 e 20: '))
while n > 20:
    n = int(input('Digite um número entre 0 e 20: '))
escolha = ex[n]
print(f'Você digitou o número \033[1;31m{escolha}.\033[m')


