soma = idadeh = 0
homem = ''
mulher = 0

for c in range(4):
    print(f'---- {c+1}° PESSOA ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma += idade
    if sexo == 'M':
        homem = nome
        idadeh = idade
        if idade > idadeh:
            idadeh = idade
    if sexo == 'F' and idade < 20:
        mulher += 1



mediaIdade = soma / 4
print(f'A media de idade do grupo é {mediaIdade:.1f}')
print(f'O homem mais velho se chama {homem.upper()} e tem {idadeh} anos.')
print(f'Ao todo temos {mulher} com menos de 20 anos.')
