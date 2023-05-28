from datetime import date
cont = contm = 0
atual = date.today().year

for c in range(0, 7):
    ano = int(input(f'Em que ano a {c+1}° nasceu? '))
    idade = atual - ano
    if idade >= 18:
        cont += 1
    elif idade < 18:
        contm += 1
print(f'Tivemos {cont} maiores')
print(f'Tivemos {contm} menores')
