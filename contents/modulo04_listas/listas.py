# Inicia o código
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

# Funções:

"""Quantidade de itens na lista"""
print(len(lista3))

"""Valor mínimo da lista"""
print(min(lista3))

"""Valor máximo da lista"""
print(max(lista3))

# Converter range ou strings para lista

"""Range"""
lista7 = list(range(10))
print(lista7)

"""Strings"""
lista8 = list("Curso de Python")
print(lista8)

# Verificar se há algo dentro da lista

if 8 in lista7:
    print("Este elemento está dentro da lista.")
else:
    print("Este elemento não está dentro da lista")

# Alterar valores da lista

lista9 = ["gato", "cachorro", "peixe", "cavalo", "tubarão", "girafa"]
print(lista9)

"""Alterando apenas um valor"""
lista9[1] = "cavalo"
print(lista9)

"""Alterando vários valores de uma vez"""
lista9[1:4] = ["águia", "morcego", "elefante"]
print(lista9)

# Visualizando o index da lista

lista10 = ["carro", "barco", "avião"]
print(lista10)

for x in range(len(lista10)):
    print(x, lista10[x])

# Adicionando um novo item na lista
"""Obs: Também é possível adicionar um novo item na lista utilizando '.insert' ou '.extend' após a lista """

lista10.append("moto")
print(lista10)

# Adicionando vários itens de uma vez na lista (append ou extend)

lista10.extend(["bicicleta", "navio"])
print(lista10)

# Removendo um item na lista
# Obs: Pode ser utilizado '.pop()' ou 'del lista10[_]' para remover o item de acordo com o seu index. Ex: 0, 1, 2, 3.

lista10.remove("navio")
print(lista10)

# Deletar uma lista

del lista10

# Apagar todos os itens na lista

lista11 = ["produto 1", "produto 2", "produto 3"]
lista11.clear()
print(lista11)

# Ordenar itens na lista

# Crescente

"""Strings"""
carrinho_de_compras = ["pão", "carne", "verduras", "alface"]
carrinho_de_compras.sort()
print(carrinho_de_compras)

""""Números"""
lista12 = [1, 50, 23, 67, 100]
lista12.sort()
print(lista12)

# Decrescente

lista12.sort(reverse = True)
print(lista12)

# Finaliza o código
print("-" * 99)
