# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
valor3 = float(input('Digite o terceiro valor: '))

if valor1 > valor2 and valor1 > valor3:
   maior = valor1
elif valor2 > valor1 and valor2 > valor3:
   maior = valor2
elif valor3 > valor1 and valor3 > valor2:
   maior = valor3

if valor1 < valor2 and valor1 < valor3:
   menor = valor1
elif valor2 < valor1 and valor2 < valor3:
   menor = valor2
elif valor3 < valor1 and valor3 < valor2:
   menor = valor3

print(f'O maior valor é: {maior :.0f}')
print(f'O menor valor é: {menor :.0f}')

# simplificando
print(f'O maior valor é: {max(valor1, valor2, valor3) :.0f}')
print(f'O menor valor é: {min(valor1, valor2, valor3) :.0f}')