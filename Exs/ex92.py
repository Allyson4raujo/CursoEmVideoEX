from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - ano
dados['ctps'] = int(input('Carteira de trabalho (Digite 0 se não tiver): '))
if dados['ctps'] != 0:
    dados['contrataçao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contrataçao'] + 35) - datetime.now().year)
print('=-'*30)
for i, v in dados.items():
    print(f'  -{i} tem o valor {v}')