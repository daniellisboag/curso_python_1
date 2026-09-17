valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))

# Soma
print('A soma é {}'.format(valor1 + valor2))

# Subtração
print('A subtração é {}'.format(valor1 - valor2))

# Multiplicação
print('A multiplicação é {}'.format(valor1 * valor2))

# Divisão
print('A divisão é {}'.format(valor1 / valor2))

# Divisão com 3 casas decimais
print('A divisão é {:.3f}'.format(valor1 / valor2))

# Exponenciação
print('A potência é {}'.format(valor1 ** valor2))

# Divisão inteira
print('A divisão inteira é {}'.format(valor1 // valor2))

# Módulo (resto da divisão)
print('O resto da divisão é {}'.format(valor1 % valor2))

# Deixar 2 print na mesma linha
print('A soma é {}'.format(valor1 + valor2), end = ' ')
print('A soma é {}'.format(valor1 + valor2))

# Quebrar a linha
print('A soma é \n {}'.format(valor1 + valor2))