exp = str(input('Digite a expressão: '))
if exp.count('(') == exp.count(')'):
    print('Expressão válida.')
else:
    print('Expressão inválida.')