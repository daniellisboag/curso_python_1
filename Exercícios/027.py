# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Exemplo: Ana Maria de Souza
# Primeiro: Ana
# Último: Souza

nome = input('Digite o seu nome completo: ')
print(f'Primeiro nome: {nome.split()[0]}')
print(f'Ultimo nome: {nome.split()[-1]}')