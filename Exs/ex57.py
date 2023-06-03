#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.

sexo = str(input('Digite seu sexo[M/F]: ')).upper().strip()
while sexo not in 'MF':
    print('Dados inválidos. Digite novamente')
    sexo = str(input('Digite seu sexo[M/F]: ')).upper().strip()
print(f'\033[1;32mSEXO({sexo})REGISTRADO COM SUCESSO!\033[m')

