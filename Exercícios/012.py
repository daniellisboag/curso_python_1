# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

valor = float(input('Digite o valor do produto: R$'))
print('O novo valor do produto com 5% de desconto fica R${:.2f}'.format(valor - (valor * 0.05)))