def notas(*n, sit=False):
    total = len(n)
    maior = max(n)
    menor = min(n)
    media = (sum(n)) / total
    if sit:
        if media < 6:
            sit = 'RUIM'
        elif media >= 6 and media <= 7:
            sit = 'MEDIA'
        else:
            sit = 'BOM'
        resultado = {'total': total, 'maior': maior, 'menor': menor, 'média': media, 'sit': sit}
    else:
        resultado = {'total': total, 'maior': maior, 'menor': menor, 'média': media}
    return resultado

#programa principal
resp = notas(5.5, 2.5,1.5, sit=False)
print(resp)
