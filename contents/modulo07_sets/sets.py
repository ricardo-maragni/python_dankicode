"""
Listas: Coleção ordenada, mutável e que permite valores duplicados
Tuplas: Coleção ordenada, imutável e que permite valores duplicados
Dicionarios: Coleção não ordenada, mutável e que não permite valores duplicados
Sets: Coleção não ordenada, imutável e que não permite valores duplicados
"""

# Os sets também são conhecidos como conjuntos

conjunto = {"item1", "item2", "item3"}
print(type(conjunto))
print(conjunto)
print(len(conjunto))

# Adicionar um item ao conjunto

conjunto.add("item4")
print(conjunto)

# Adicionar vários itens ao conjunto

novos_itens = {"item5", "item6", "item7", "item8", "item9"}
conjunto.update(novos_itens)
print(conjunto)

# Remover elementos

conjunto.remove("item4")
conjunto.discard("item5")
print(conjunto)

# Limpar o conjunto

conjunto.clear()
print(conjunto)
