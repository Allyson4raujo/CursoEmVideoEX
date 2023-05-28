#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('----É triangulo ou não?----!')
reta1 = float(input('Digite o valor da primera reta: '))
reta2 = float(input('Digite o valor da segunda reta: '))
reta3 = float(input('Digite  valor da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    print('Com esses valores É POSSIVEL formar um triangulo!')
else:
    print('Com esses valores NÃO É POSSIVEL formar um triangulo!')