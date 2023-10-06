dados = []
cont = 0
escolha = ''
media = 0
while True:
    dadosd = {}
    dadosd['nome'] = str(input('Digite seu nome: ')).strip().capitalize()
    dadosd['sexo'] = str(input('Digite o sexo [M/F]: ')).strip()[0].upper()
    while dadosd['sexo'] not in 'MF':
        print('Valor inválido! Digite M ou F ')
        dadosd['sexo'] = str(input('Digite o sexo [M/F]: ')).strip()[0].upper()
    dadosd['idade'] = int(input('Digite idade: '))
    media += dadosd['idade']
    escolha = str(input('Deseja continuar [S/N]? ')).upper().strip()
    while escolha not in 'SN':
        print('Valor inválido! Digite S ou N')
        escolha = str(input('Deseja continuar [S/N]? ')).upper().strip()
    dados.append(dadosd)
    cont += 1
    if escolha in 'N':
        break
print('=-'*30)
print(f'A)  Ao todo temos {cont} pessoas cadastradas.')
media = (media / cont)
print(f'B)  A média de idade é {media:.2f} anos')
print(f'C)  As mulheres cadastradas foram ', end='')
for p in dados:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print(f'\nD)  Lista de pessoas  que estão acima da média: ')
for i in dados:
    if i['idade'] > media:
        print(f'     Nome = {i["nome"]}; sexo = {i["sexo"]}; Idade = {i["idade"]};')
