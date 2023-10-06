import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.real(p)} é {(moeda.metade(p, True))}')
print(f'O dobro de {moeda.real(p)} é {(moeda.dobro(p, True))}')
print(f'Aumento 10%, temos {(moeda.aumentar(p, 10,f=True))}')