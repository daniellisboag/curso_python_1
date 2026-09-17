# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 para viagens mais longas.

distancia = float(input('Digite a disância da viagem: '))

if distancia <= 200:
   print(f'O valor da passagem será R${distancia * 0.50 :.2f}')
else:
   print(f'O valor da passagem será R${distancia * 0.45 :.2f}')

# Simplificando
print(f'O valor da passagem será R${distancia * 0.50 :.2f}' if distancia <= 200 else f'O valor da passagem será R${distancia * 0.45 :.2f}')