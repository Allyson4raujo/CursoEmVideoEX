valor = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento: '))
prestaçao = valor / (anos * 12)
print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos, a prestação vai ficar R${prestaçao:.2f}')
if prestaçao > salario * 30 / 100:
    print('O valor passa de 30% do seu salário.\nFinanciamento negado!')
else:
    print('Financiamento aprovado!')

