# Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digitre a segunda nota: '))
media = (n1 + n2) / 2
print(f'A media entre {n1} e {n2} é igual {media:.2f} ')
