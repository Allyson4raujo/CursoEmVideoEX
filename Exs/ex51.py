def linha():
    print('=' * 20)

linha()
print('10 TERMOS DE UMA PA')
linha()

p = int(input('Digite o primeiro termo: '))
r = int(input('Razão: '))
for c in range(p, p + 10 * r, r):
    print(f'{c} => ', end='')
print('FIM')
