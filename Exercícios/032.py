# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from calendar import isleap
from datetime import datetime

ano = int(input('Digite um ano: '))

# Se o ano for igual a 0, retornara o ano atual.
if ano == 0:
   # Verifica o ano atual
   ano = datetime.now().year

if isleap(ano) == True:
   print(f'O ano {ano} é bissexto.')
else:
   print(f'O ano {ano} não é bissexto.')

# Simplificando
print(f'O ano {ano} é bissexto.' if isleap(ano) == True else f'O ano {ano} não é bissexto.')