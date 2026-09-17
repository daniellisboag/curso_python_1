# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separarados.
# Exemplo:
# Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

numero = int(input('Digite um número de 0 a 9999: '))
valor = str(numero).zfill(4)
print(f'Unidade: {valor[3]}\nDezena: {valor[2]}\nCentena: {valor[1]}\nMilhar: {valor[0]}')

# Ou
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'Unidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}')