dinheiro = float(input('Quanto dinheiro você tem na carteira? R$'))
cotacao = 5.03 # Cotação do dólar em reais
dolares = dinheiro / cotacao

print(f'Com R${dinheiro:.2f} você pode comprar US${dolares:.2f}')
