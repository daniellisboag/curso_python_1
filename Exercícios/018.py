# Faça um programa que leia um ângulo qualquer e mostre na tela o valor
# do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

valor = float(input('Digite um valor: '))
print('O valor de seno é {:.2f}\nO valor de cosseno é {:.2f}\nO valor da tangente é {:.2f}'.format(sin(radians(valor)), cos(radians(valor)), tan(radians(valor))))