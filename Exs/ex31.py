# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distancia da sua viagem ? '))
print(f'Você está prestes a começar uma viagem de {distancia:.1f}Km')
if distancia <= 200:
    vviagem = distancia * 0.50
    print(f'O preço da sua passagem será R${vviagem:.2f}')
elif distancia > 200:
    vviagem = distancia * 0.45
    print(f'O preço da sua passagem será R${vviagem:.2f}')

