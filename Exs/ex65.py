escolha = 'S'
soma = cont = media = maior = menor = 0
while escolha == 'S':
    n = int(input('Digite um valor: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    escolha = str(input('Deseja continuar [S/N] ? ')).upper().strip()

media = soma / cont
print(f'Media {media:.2f}\nMaior {maior}\nMenor {menor}')