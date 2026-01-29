# Slicing
# Slicing é usado para acessar partes de listas ou strings.
# A estrutura é: [início : fim : passo]

# ======================
# LISTAS
# ======================

lista5 = [True, "chicago", 2.5, False, 4, 8, 9]

# Mostra todos os elementos da lista
print(lista5[::])

# Começa do índice 1 até o final
print(lista5[1:])

# Começa do índice 2 até o final
print(lista5[2:])

# Do início até o índice 2 (o 3 não entra)
print(lista5[:3])

# Do início até o índice 3 (o 4 não entra)
print(lista5[:4])

# Do índice 1 até o 3 (o 4 não entra)
print(lista5[1:4])

# Do índice 1 até o 5, pulando de 2 em 2
print(lista5[1:6:2])

# ======================
# STRINGS
# ======================

nome5 = "terra"

# Mostra toda a string
print(nome5[::])

# Começa da letra no índice 1 até o final
print(nome5[1:])

# Do início até o índice 2 (o 3 não entra)
print(nome5[:3])

# Do índice 2 até o 3 (o 4 não entra)
print(nome5[2:4])

# Do índice 2 até o 4, pulando de 2 em 2
print(nome5[2:5:2])
