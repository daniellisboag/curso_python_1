# Escreva um programa que pergunte o salário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00 calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu salário: R$'))

if salario > 1250:
   print(f'Seu novo salário terá um aumento de 10% e será R${salario + (salario * 0.10) :.2f}')
elif salario <= 1250:
   print(f'Seu novo salário terá um aumento de 15% e será R${salario + (salario * 0.15) :.2f}')