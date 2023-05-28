# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang = int(input('Digite o ângulo que você deseja: '))
seno = math.radians(math.sin(ang))
cos = math.radians(math.cos(ang))
tan = math.radians(math.tan(ang))
print(f'seno: {seno:.2f}\n'
      f'cosseno: {cos:.2f}\n'
      f'tangente: {tan:.2f}')


