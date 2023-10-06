print('  CONTROLE DE TERRENO')
print('-'*25)
def area():
    l = float(input('Largura (m): '))
    c = float(input('Comprimento (m): '))
    a = l * c
    print(f'A área de um terreno {l} x {c} é de {a}m² ')

area()