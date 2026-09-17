# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua
# área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de
# tinta pinta uma área de 2M².

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
print('Área a ser pintada: {:.2f}Mts²'.format(largura * altura))
print('Quantidade de tinta necessária: {:.2f}Lts'.format((largura * altura) / 2))