# Escreva um programa que pergunte a quantidade de kilometros percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o
# carro custa R$60 por dia e R$0,15 por kilometro rodado.

kilometros = float(input('Quantos kilometros foi perrcorido? '))
dias = int(input('Por quantos dias ele foi alugado? '))
print('Você percorreu {:.2f}km, por {:.0f} dia(s). O valor a ser pago é R${:.2f}'.format(kilometros, dias, (kilometros * 0.15) + (dias * 60)))