valor = int(input('Digite um valor para calcular o fatorial: '))
fatorial = 1
print(f'Calculando {valor}! = ', end='')
for c in range(valor, 0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='') #Muito bom
    fatorial *= c
print(f'{fatorial}')
#comentario linha 4
# O C é = ao valor que o usuario digitar, com isso na primeira iteração vai ser fatorial x valor inserido