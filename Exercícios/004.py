# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

valor = input('Digite algo: ')
print('O tipo primitivo é:', type(valor))
print('É um valor que tem somente espaços?', valor.isspace())
print('É um valor numérico?', valor.isnumeric())
print('É um valor alfabético?', valor.isalpha())
print('É um valor alfanumérico, isto é contém números ou letras?', valor.isalnum())
print('É um valor alfabético com todas letras maiúsculas?', valor.isupper())
print('É um valor alfabético com todas letras minúsculas?', valor.islower())

# Capitalizada significa que o valor tem letras maiúsculas e minúsculas.
print('É um valor capitalizado?', valor.istitle())