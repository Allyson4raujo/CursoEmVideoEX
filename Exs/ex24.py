#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cit = str(input('Em que cidade você nasceu? ')).strip().capitalize()
dividir = cit.upper().split()
print(dividir[0] == "SANTO")
