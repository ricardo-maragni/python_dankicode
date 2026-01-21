"""
Python - Comandos de controle condicional

if, else e elif
"""

x = 3
y = 3

if y > x:
    print("y é maior do que x")
elif y < x:
    print("y é menor do que x")
else:  # Aqui poderia ter sido usado "elif y == x:"
    print("y não é menor nem maior que x")

print("Código fora do bloco condicional")
print(y > x)
print(y < x)
print(y == x)
