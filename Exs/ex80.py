valores = []
for c in range(0, 5):
    v = int(input('Digite um valor: '))
    if c == 0 or v > valores[-1]:
        valores.append(v)
    else:
        posicao = 0
        while posicao < len(valores):                                             #Varredura em toda a lista (valores).
            if v <= valores[posicao]:
                valores.insert(posicao, v)
                print(f'Adicionado na posição {posicao}')
                break
            posicao += 1



print(valores)