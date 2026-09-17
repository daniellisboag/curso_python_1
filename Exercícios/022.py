# Crie um programa que leia o nome completo de uma pessoa e mostre:

nome = str(input('Digite seu nome: ')).strip()

# O nome com todas as letras maiúsculas.
print(f'Seu nome com todas as letras maiúsculas: {nome.upper()}')

# O nome com todas as letras minúsculas.
print(f'Seu nome com todas as letras minúsculas: {nome.lower()}')

# Quantas letras ao todo (sem considerar espaços).
print(f'Seu nome contém: {len(nome.replace(' ', ''))} caraceteres.')

#Ou
print(f'Seu nome contém: {len(''.join(nome.split()))} caraceteres.')

# Quantas leras tem o primeiro nome.
print(f'O primeiro nome tem {len(nome.split()[0])} caracteres.')