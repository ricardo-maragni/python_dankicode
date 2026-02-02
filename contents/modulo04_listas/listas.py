print("-" * 99)

# Lista contendo apenas strings (textos)
lista = ["chicago", "queens", "salvador", "pernambuco"]
print(lista)

# Lista contendo apenas números inteiros
lista2 = [2, 3, 7, 8, 10]
print(lista2)

# Lista contendo números decimais (float)
lista3 = [2.0, 3.5, 6.3]
print(lista3)

# Lista contendo valores booleanos
lista4 = [True, False]
print(lista4)

# Lista mista: pode conter diferentes tipos de dados
lista5 = [True, "chicago", 2.5, False, 4, 8, 9]
print(lista5)

# Mostra o tipo da variável lista5 (list)
print(type(lista5))

# Visualizar os elementos em determinadas posições do index. Obs: O index começa em 0
print(lista5[0]) # Visualiza o primeiro valor da lista
print(lista5[1]) # Visualiza o segundo valor da lista 
print(lista5[2]) # Visualiza o terceiro valor da lista 
print(lista5[-1]) # Visualiza o ÚLTIMO valor da lista 

# Slicing

"""Números"""

print(lista5[::])
print(lista5[1:])
print(lista5[2:])
print(lista5[:3])
print(lista5[:4])
print(lista5[1:4])
print(lista5[1:6:2])

"""Strings"""

nome5 = "terra"

print(nome5[::])
print(nome5[1:])
print(nome5[:3])
print(nome5[2:4])
print(nome5[2:5:2])

print("-" * 99)

# Funções:

"""Quantidade de itens na lista"""
print(len(lista3))

"""Valor mínimo da lista"""
print(min(lista3))

"""Valor máximo da lista"""
print(max(lista3))
