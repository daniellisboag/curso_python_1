# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from random import choice

primeiro = input('Digite o nome do primeiro aluno: ')
segundo = input('Digite o nome do segundo aluno: ')
terceiro = input('Digite o nome do terceiro aluno: ')
quarto = input('Digite o nome do quarto aluno: ')
print('O aluno sorteado para apagar o quadro é {}.'.format(choice([primeiro, segundo, terceiro, quarto])))