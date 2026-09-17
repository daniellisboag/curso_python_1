# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt, hypot

oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
print('O cateto oposto é {}\nO cateto adjacente é {}\nO comprimento da hipotenusa é {:.2f}'.format(oposto, adjacente, hypot(oposto, adjacente)))

# Ou
print('O cateto oposto é {}\nO cateto adjacente é {}\nO comprimento da hipotenusa é {:.2f}'.format(oposto, adjacente, sqrt((oposto ** 2) + (adjacente ** 2))))

# Ou
print('O cateto oposto é {}\nO cateto adjacente é {}\nO comprimento da hipotenusa é {:.2f}'.format(oposto, adjacente, ((oposto ** 2) + (adjacente ** 2)) ** 0.5))

# Ou
print('O cateto oposto é {}\nO cateto adjacente é {}\nO comprimento da hipotenusa é {:.2f}'.format(oposto, adjacente, pow((oposto ** 2) + (adjacente ** 2), 0.5)))