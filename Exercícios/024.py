# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.

nome = input('Digite o nome da cidade: ').strip()
texto = nome.split()
print(f'A cidade {"começa" if texto[0].lower() == "santo" else "não começa"} com Santo no nome.')