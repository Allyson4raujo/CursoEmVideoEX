#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
#média atingida: - Média abaixo de 5.0: REPROVADO - Média entre 5.0 e 6.9: RECUPERAÇÃO - Média 7.0 ou superior: APROVAD)

nota = []
for c in range(0, 2):
    nota.append(float(input(f'Digite sua {c+1}° nota: ')))
media = sum(nota) / len(nota)
print('Tirando', ', '.join(map(str, nota)), end='')
print(f' sua media fica {media:.2f}')
if media < 5:
    print('O aluno foi \033[1;31mREPROVADO.\033[m')
elif media >= 5 and media <= 6.9:
    print('O aluno está de \033[1;33mRECUPERAÇÃO.\033[m')
elif media >= 7:
    print('O aluno está \033[1;32mAPROVADO.\033[m')



