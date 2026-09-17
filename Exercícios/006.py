# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

valor = int(input('Digite um número: '))
print('O dobro de {} é {}'.format(valor, valor * 2))
print('O triplo de {} é {}'.format(valor, valor * 3))
print('A raiz quadrada de {} é {:.2f}'.format(valor, valor ** 0.5))

# Ou
print('A raiz quadrada de {} é {:.2f}'.format(valor, pow(valor, 0.5)))