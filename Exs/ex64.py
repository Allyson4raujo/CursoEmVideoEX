soma = cont = 0
while True:
    n = int(input('Digite um número [999 flag]: '))
    if n != 999:
        cont += 1
        soma += n
    else:
        break

print(f'Foram digitados {cont} números.\nA soma é {soma}')