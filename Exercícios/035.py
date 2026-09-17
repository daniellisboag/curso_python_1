# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

comprimento1 = float(input('Digite o primeiro comprimento: '))
comprimento2 = float(input('Digite o segundo comprimento: '))
comprimento3 = float(input('Digite o terceiro comprimento: '))

if (comprimento1 + comprimento2 > comprimento3) and (comprimento1 + comprimento3 > comprimento2) and (comprimento2 + comprimento3 > comprimento1):
   print('Os comprimentos podem formar um triângulo!')
else:
   print('Os comprimentos não podem formar um triângulo!')