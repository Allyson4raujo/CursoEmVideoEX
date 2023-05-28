#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
# também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {atual}')
if idade == 18:
    print(f'Você tem que se alistar imediatamente.')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos para você se alistar.\nSeu alistamento será {atual + (18 - idade)}')

elif idade > 18:
    print(f'Você ja deveria ter se alistado a {idade - 18} anos.\nSeu alistamento foi em {atual - (idade - 18)}')
print('FIM DO PROGRAMA.')