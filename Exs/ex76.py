produtos = ('Lápis', 1.50, 'Borracha', 2.00, 'Caderno', 5.90, 'Estojo', 25, 'Transferidor', 4.20,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}', end='')
    else:
        print(f'R$ {produtos[c]:>8.2f}')
#for c in produtos:
    #print(f'{c}')