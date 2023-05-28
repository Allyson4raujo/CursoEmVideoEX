#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores
# a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

s = float(input('Qual o salário do funcionario R$: '))
if s > 1250:
    print(f'O novo salário será R${s + (s*10/100):.2f} Aumento de 10%')
else:
    print(f'O novo salário será R${s + (s*15/100):.2f} Aumento de 15%')