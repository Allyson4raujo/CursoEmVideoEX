while True:
    n = int(input('QUal tabuada deseja ver ? '))
    print('-' * 30)
    if n < 0:
        break
    else:
        for c in range(1, 11):
            mult = n*c
            print(f'{n:2} x{c:2} = {mult}')
    print('-' * 30)
print('Fim do programa.')

