# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

aleatorio = randint(0, 5)
numero = int(input('Digite um número de 0 a 5: '))
print('Aguarde...')

# Espera 1.5 segundos para executar o próximo comando
sleep(1.5)

# Verifica se o número digitado é igual ao que foi sorteado.
if numero == aleatorio:
   print(f'O número sorteado foi {aleatorio}, você escolheu o número {numero}.')
   print('Parabéns! Você acertou o número que o computador sorteou.')
else:
   print(f'O número sorteado foi {aleatorio}, você escolheu o número {numero}.')
   print('Que pena! Você não acertou o número que o computador sorteou.')