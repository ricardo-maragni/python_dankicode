"""
Listas: Coleção ordenada, mutável e que permite valores duplicados
Tuplas: Coleção ordenada, imutável e que permite valores duplicados
Dicionarios: Coleção não ordenada, mutável e que não permite valores duplicados
"""

lista = ["item1", "item2"]

tupla = ("item1", "item2")

dicionario1 = {"chave1" : "Gabriel", "chave2" : 1993, "chave3" : True}

print(dicionario1)

dicionario2 = {
    "nome": "Bruna",
    "idade": 27,
    "nacionalidade": "brasileira" 
}

print(dicionario2)

print(dicionario2["idade"])

print(dicionario2.get("idade"))

print(dicionario2.keys())

print(len(dicionario2))

print(dicionario2.values())

if "idade" in dicionario2:
    print("A idade existe")

print(dicionario2.items())

# Copiar dicionário em outro

dicionario3 = dicionario2.copy()

# Modificar itens de um dicionário

print(dicionario2["nome"])
dicionario2["nome"] = "Pedro"
print(dicionario2["nome"])

# Adicionar chave

print(dicionario2)
dicionario2.update({"estado":"Rio de Janeiro"})
print(dicionario2)


# Remover chave

dicionario2.popitem() # remove a última chave

dicionario2.pop("idade") # remove uma chave específica

del dicionario2["nacionalidade"] # remover uma chave específica

print(dicionario2)

# Limpa o dicionário

dicionario2.clear()
print(dicionario2)

# Cópia do dicionario2

print(dicionario3)
