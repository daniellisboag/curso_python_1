# Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.

valor = float(input('Digite um valor em metros: '))
print('{} metros convertidos para centímetros é {:.2f}cm'.format(valor, valor * 100))
print('{} metros convertidos para milímetros é {:.2f}mm'.format(valor, valor * 1000))