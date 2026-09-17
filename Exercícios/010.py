# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere: US$1,00 = R$3,27

valor = float(input('Digite quantos reais você tem: R$'))
print('Você pode comprar US${:.2f} com R$ {}'.format(valor / 3.27, valor))