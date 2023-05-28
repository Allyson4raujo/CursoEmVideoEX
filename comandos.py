"""
- Len() Em uma string ela retorna a quantidade de caracteres que possui, ou seja, o comprimento. Sintaxe: len(frase)
- Count() Retorna a quantidade de vezes que um mesmo elemento está contido numa lista. Sintaxe: frase.count('a')
outra possibilidade é usar o count com fatiamento por exemplo: frase.count('a',0,10)(buscando o 'a' de 0 até 10)
- Find() Vai te dizer a partir de que momento ele encontrou certa string. Sintaxe: frase.find('a')
o find pode ser ultilizado com letra ou com uma palavra itneira. Caso ele não encontre a letra ou a palavra ele retorna
- Replace() Ele localiza e substitui uma palavra por outra. Ex: nome = 'andrews' - nome.replace('andrews','allyson')
 o nome passa a ser 'allyson'.
- Upper() Coloca em maiúsculo. Sintaxe: frase.upper()
- Lower() Coloca em minúsculo. Sintaxe: frase.lower()

- Captalize() Coloca só o primeiro caractere em maiúsculo. Ex: nome = 'andrews braga de araujo' nome.captalize() nome = 'Andrews Braga De Araujo'
- Title() Ele analisa quantas palavras tem na frase, baseado na posição dos espaços e coloca suas iniciais em maiúsculo.
- Strip() Remove todos os espaços do começo e do final. frase.strip()
- Split() Refaz os índices, onde tiver espaço ele separa a palavra e cria novos índices.
- join() Junta todos os elemttos. Sintaxe: join(frase) pode ser ultilizado da seguinte forma: '-'.join(frase)
ele vai juntar as palavras e na junção colocar esse ('-' traço) pode ser feito com espaço:
"""
