valor = float(input('Digite o valor das compras: '))
print('Formas de pagamento')
pagamentos = ('Á vista dinheiro/débito', 'Pix', '2x no crédito', '3x ou mais no crédito')
for i, v in enumerate(pagamentos):
    print(f'[{i}] {v}')
escolha = int(input('Escolha: '))

if escolha == 0:
    total = valor - (valor * 10 / 100)
elif escolha == 1:
    total = valor - (valor * 5 / 100)
elif escolha == 2:
    total = valor
elif escolha == 3:
    total = valor + (valor * 20 / 100)
print(f'Sua compra de R${valor:.2f} vai custar R${total:.2f} no final')