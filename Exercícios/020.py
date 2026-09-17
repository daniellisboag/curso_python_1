# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos
# dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

primeiro = input('Digite o nome do primeiro aluno: ')
segundo = input('Digite o nome do segundo aluno: ')
terceiro = input('Digite o nome do terceiro aluno: ')
quarto = input('Digite o nome do quarto aluno: ')
ordem = [primeiro, segundo, terceiro, quarto]
shuffle(ordem)
print(f'A ordem de apresentação será {ordem}')