"""
Exercício - Trocar variáveis
"""

# Variáveis que queremos trocar

x = input("Insira o valor de x: ")
y = input("Insira o valor de y: ")


# Variável temporária

temp = x
x = y
y = temp

# Resultado

print(f"O valor de x depois da troca: {x}")
print(f"O valor de y depois da troca: {y}")
