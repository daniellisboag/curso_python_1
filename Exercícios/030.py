# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou Ímpar.

numero = int(input('Digite um número para verificar se ele é ímpar ou par: '))

if numero % 2 == 0:
   print(f'O número {numero} é par.')
else:
   print(f'O número {numero} é ímpar.')