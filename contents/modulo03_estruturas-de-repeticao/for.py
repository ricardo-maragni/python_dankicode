
# 1
print("Exemplo 1 — Percorrendo uma string")

palavra = "pernambuco"
for letra in palavra:
    print(letra)

# 2
print("Exemplo 2 — for com range simples")

for numero in range(6):
    print(numero)

# 3
print("Exemplo 3 — range com início e fim")

for valor in range(5, 8):
    print(valor)

# 4
print("Exemplo 4 — range com passo")

for numero_par in range(0, 6, 2):
    print(numero_par)

# 5
print("Exemplo 5 — for com else")

for contador in range(6):
    print(contador)
else:
    print("Chegamos ao fim")
