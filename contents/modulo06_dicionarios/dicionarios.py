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
