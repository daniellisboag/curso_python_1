tempo = int(input('Quantos ano tem seu carro? '))

if tempo <= 3:
   print('Seu carro é novo.')
else:
   print('Seu carro é velho.')
print('Fim')

# Simplificando
print('Seu carro é novo.' if tempo <= 3 else 'Seu carro é velho')
print('Fim')

# ---------------------------------------------------------------------------------------------------------

nome = input('Qual é o seu nome? ')
if nome == 'Daniel':
   print('Que nome lindo você tem!')
else:
   print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')

# ---------------------------------------------------------------------------------------------------------

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

print(f'A sua média foi {(nota1 + nota2) / 2 :.1f}')
if (nota1 + nota2) / 2 >= 6.0:
   print('Sua média foi boa! Parabéns!')
else:
   print('Sua média foi ruim! Estude mais!')

# Simplificando
print('Sua média foi boa! Parabéns!' if (nota1 + nota2) / 2 >= 6.0 else 'Sua média foi ruim! Estude mais!')