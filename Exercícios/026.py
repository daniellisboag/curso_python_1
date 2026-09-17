# Faça um programa que leia uma frase pelo teclado e mostre:

texto = input('Digite um frase: ')

# Quantas vezes aparece a letra 'A'.
print(f'A letra "A" aparece: {texto.lower().count('a')}.')

# Em que posição ela aparece a primeira vez.
print(f'A letra "A" começa na posição: {texto.strip().lower().find('a')}.')

# Em que posição ela aparece a última vez.
print(f'A letra "A" apareceu na posição: {texto.strip().lower().rfind('a')} por ultimo.')