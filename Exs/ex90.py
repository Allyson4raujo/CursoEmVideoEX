aluno = {}
aluno['nome'] = str(input('Nome: ')).capitalize().strip()
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print('=-'*30)
print(f'- Nome do aluno é {aluno["nome"]}')
print(f'- Média do aluno {aluno["nome"]} é {aluno["media"]}')
print(f'- Situação d {aluno["nome"]} é ', end='')
if aluno['media'] < 5:
    print('\033[1;31mREPROVADO!\033[m')
elif aluno['media'] >= 5 and aluno['media'] < 7:
    print('\033[1;33mRECUPERAÇÃO\033[m')
else:
    print('\033[1;35mAPROVADO!\033[m')
