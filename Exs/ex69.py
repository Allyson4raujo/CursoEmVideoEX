Cidade = Chomem = Cmulher = 0
print('-' * 23)
print('\033[1;34mCadastro de pessoas\033[m')
print('-' * 23)
while True:
        Idade = int(input('Idade: '))
        Sexo = str(input('Sexo: [M/F] '))[0].strip().upper()
        if Idade > 18:
                Cidade += 1
        if Sexo == 'M':
                Chomem += 1
        if Sexo == 'F' and Idade < 20:
                Cmulher += 1
        escolha = str(input('Deseja continuar ? [S/N] ')).upper().strip()[0]
        if escolha not in 'S':
            break
print(f'\n\033[1;34m{Cidade}\033[m pessoas tem mais de 18 anos.\n\033[1;34m{Chomem}\033[m homens ao todo.\n'
      f'\033[1;34m{Cmulher}\033[m mulheres menor que 20 anos.')