"""
Listas: Coleção ordenada, mutável e que permite valores duplicados
Tuplas: Coleção ordenada, imutável e que permite valores duplicados
Dicionarios: Coleção não ordenada, mutável e que não permite valores duplicados
Sets: Coleção não ordenada, imutável e que não permite valores duplicados
"""

# Os sets também são conhecidos como conjuntos

conjunto1 = {"item1", "item2", "item3"}
print(type(conjunto1))
print(conjunto1)
print(len(conjunto1))

# Adicionar um item ao conjunto1

conjunto1.add("item4")
print(conjunto1)

# Adicionar vários itens ao conjunto

pacote1 = {"item5", "item6", "item7", "item8", "item9"}
conjunto1.update(pacote1)

print(conjunto1)

# Remover elementos

conjunto1.remove("item4")
conjunto1.discard("item5")
print(conjunto1)

# Limpar o conjunto

conjunto1.clear()
print(conjunto1)

# Unir conjuntos

conjunto1 = {"item1", "item2", "item3"}
conjunto2 = {"item10", "item11", "item12", "item13", "item14", "item15"}
conjunto3 = conjunto1.union(conjunto2)
print(conjunto3)

# Interseção de conjuntos

conjunto4 = {1, 2, 3}
conjunto5 = {3, 4, 5}

conjunto6 = conjunto4.intersection(conjunto5)
print(conjunto6)
