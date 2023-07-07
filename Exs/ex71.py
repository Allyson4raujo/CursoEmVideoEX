def traço(v):
    return '=' * v

print(traço(20))
print('BANCO GEMEOS')
print(traço(20))

valor = int(input('Qual valor você quer sacar ?R$ '))
total = valor
cedula = 50
cont = 0

while True:
    if total >= cedula:
        total -= cedula
        cont += 1
    else:
        if cont > 0:
            print(f'Total de {cont} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        cont = 0

    if total == 0:
        break

