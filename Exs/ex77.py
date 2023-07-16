palavras = ('APRENDER',
            'PROGRAMAR',
            'LINGUAGEM',
            'PYTHON',
            'CURSO',
            'GRATIS',
            'ESTUDAR',
            'PRATICAR',
            'TRABALHAR',
            'MERCADO',
            'PROGRAMADOR',
            'FUTURO'
            )

for c in palavras:
    print(f'Na palavra {c} temos ', end='')
    for l in c:
        vogal = 'AEIOU'
        if l in vogal:
            print(f'{l}', end=' ')
    print()




