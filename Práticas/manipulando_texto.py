texto = 'Curso em Video Python'

# ------------------------------------------------------------------------------------------------
# | C | u | r | s | o | _ | e | m | _ | V | i  | d  | e  | o  | __ | P  | y  | t  | h  | o  | n  |
# | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
# ------------------------------------------------------------------------------------------------

# Mostra o 9° caractere.
print(texto[9])

# Mostra do 9° caractere até o 13° caratere sendo que 13° é excluído.
print(texto[9:13])

# Mostra do 9° caractere até o 21° caratere sendo que 21° é excluído.
print(texto[9:21])

# Mostra do 9° caractere até o 21° caractere, pulando de 2 em 2 caracteres.
print(texto[9:21:2])

# Mostra do começo até o 5° caractere, sendo que o 5° caractere é excluído.
print(texto[:5])

# Mostra do 15° caractere até o final.
print(texto[15:])

# Mostra do 9° caractere até o final pulando de 3 em 3 caracteres.
print(texto[9::3])

# Mostra a quantidade de caracteres.
print(len(texto))

# Conta quantas vezes determinado caractere aparece.
print(texto.count('o'))

# Conta quantas vezes determinado caractere aparece, com fatiamento.
print(texto.count('o', 0, 13))

# Vai mostrar em que posição ele começou.
print(texto.find('deo'))

# Vai retornar -1 pois não encontrou 'Android' dentro da string.
print(texto.find('Android'))

# Se dentro de texto tiver 'Curso' retorna 'True', se não 'False'.
print('Curso' in texto)

# Subsititui 'Python' por 'Android'.
print(texto.replace('Python', 'Android'))

# A frase passa a ter todos os caracteres maiúsculos.
print(texto.upper())

# A frase passa a ter todos os caracteres minúsculos.
print(texto.lower())

# Somente o primeiro caracetere será maiúsculo.
print(texto.capitalize())

# Analisa cada palavra e transforma todo primeiro caractere em maiúsculo.
print(texto.title())

# Remove todos os espaços do início e do fim da string.
print('   Aprenda Python  '.strip())

# Remove todos os espaços do fim da string 'r - right (direita)'.
print('   Aprenda Python  '.rstrip())

# Remove todos os espaços do início da string 'l - left (esquerda)'.
print('   Aprenda Python  '.lstrip())

# Divide a frase onde estiver espaços.
print(texto.split())

# Faz a junção das palavras separadas e coloca um traço '-' nos espaços.
print('-'.join(texto.split()))