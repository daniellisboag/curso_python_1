print('Olá, mundo!')
print(7 + 4)
print('7' + '4')
print('7', '4')
nome = 'Daniel'
idade = 24
peso = 66.5
print(nome, idade, peso)
print(nome + idade + peso) # Erro

nome = input('Qual é o seu nome? ')
idade = input('Quantos anos você tem? ')
peso = input('Quantos kilos você pesa? ')
print(nome, idade, peso)

# 1° Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de
# acordo com o valor digitado.

nome = input('Qual é o seu nome? ')
print('Olá', nome, '! Prazer em te conhcer')

# 2° Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma
# mensagem com a data formatada.

dia = input('Dia: ')
mes = input('Mês: ')
ano = input('Ano: ')
print('Você nasceu no dia', dia, 'de', mes, 'de', ano, '. Correto?')

# 3° Crie um script Python que leia dois números e tente mostrar a soma entre eles.

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
print('A soma entre', valor1, 'e', valor2, 'é: ', valor1 + valor2)
print('A soma é', valor1 + valor2)

# Ou
print('A soma vale {}'.format(valor1 + valor2))
print('A soma entre {} e {} vale {}'.format(valor1, valor2, (valor1 + valor2)))

# --------------------------------------------------------------------------------------------------------------------

valor = input('Digite algo: ')

# isnumeric() Se for numérico retornara 'True' se não for numérico retornara 'False'.
print(valor.isnumeric())

# isalpha() Se for alfabético retornara 'True' se não for alfabético retornara 'False'.
print(valor.isalpha())

# isalnum() se for alfabético e numérico retornara 'True' se não for alfabético mas se for numérico (e vice versa)
# retornara 'True'. Se estiver somento espaçamento retornara 'False'.
print(valor.isalnum())

# --------------------------------------------------------------------------------------------------------------------

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))

# + 20 caracteres a direita
print('Prazer em te conhecer {:20}!'.format(nome))

# Alinhar texto a esquerda
print('Prazer em te conhecer {:>20}!'.format(nome))

# Alinhar texto a direita
print('Prazer em te conhecer {:<20}!'.format(nome))

# Alinhar texto ao centro
print('Prazer em te conhecer {:^20}!'.format(nome))

# Alinhar texto ao centro e colocar sinal de igual '=' antes e depois do nome
print('Prazer em te conhecer {:=^20}!'.format(nome))