# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.

velocidade = float(input('Digite a velocidade atual do carro: '))

if velocidade > 80:
   print('Velocidade máxima 80Km/h')
   print(f'Você está a {velocidade :.0f}Km/h e foi multado.')
   print(f'O valor da multa é R${(velocidade - 80) * 7 :.2f}')
else:
   print(f'Você está a {velocidade :.0f}Km/h e está dentro do limite de velocidade que é 80Km/h.')