# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário do funcionário: R$'))
print('O novo salário com 15% de aumento fica R${:.2f}'.format(salario + (salario * 0.15)))