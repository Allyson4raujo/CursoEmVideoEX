from datetime import datetime

def voto(ano):
    atual = datetime.now().year
    idade = atual - ano
    if idade < 16:
        return f'Com idade {idade} anos. \033[1;31mVOTO NEGADO\033[m'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com idade {idade} anos. \033[1;33mVOTO OPICIONAL\033[m'
    else:
        return f'Com idade {idade} anos. \033[1;32m VOTO OBRIGATORIO\033[m'



a = int(input('Digite o ano de nascimento: '))
print(voto(a))

