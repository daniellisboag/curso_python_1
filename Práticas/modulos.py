# Importa biblioteca matemática

import math

# Da biblioteca matemática importe raiz quadrada (sqrt) e arredondamento para cima (floor)
from math import sqrt, floor
valor = int(input('Digite um número: '))
print('A raiz quadrada de {} é igual a {}'.format(valor, floor(sqrt(valor))))

# Raiz quadrada (math.sqrt)
print('A raiz quadrada de {} é igual a {}'.format(valor, math.sqrt(valor)))

# Duas casas decimais
print('A raiz quadrada de {} é igual a {:.2f}'.format(valor, math.sqrt(valor)))

# Arredonda para cima (math.ceil)
print('A raiz quadrada de {} é igual a {}'.format(valor, math.ceil(math.sqrt(valor))))

# Arredonda para baixo (math.floor)
print('A raiz quadrada de {} é igual a {}'.format(valor, math.floor(math.sqrt(valor))))

import random

# Gera um número float de 0 a 1
numero = random.random()

# Gera um número inteiro de 1 até 10
numero = random.randint(1, 10)
print(numero)

# Importa biblioteca emoji

import emoji

print(emoji.emojize("Olá, Mundo :slightly_smiling_face:"))