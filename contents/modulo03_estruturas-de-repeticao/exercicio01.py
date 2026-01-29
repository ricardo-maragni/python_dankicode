# 01 - Escreva um programa que leia 5 valores e encontre o maior e o menor deles. Mostre o resultado.

valores = []

# Leitura dos 5 valores
for x in range(5):
    numero = float(input(f"Digite o {x + 1}º valor: "))
    valores.append(numero)

# Encontrando maior e menor
maior = max(valores)
menor = min(valores)

# Exibindo o resultado
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
