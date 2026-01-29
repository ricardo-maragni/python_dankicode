"""
Como descobrir se um número é par ou impar
"""

# A porcentagem serve para você descobrir o 'resto' de uma divisão no Python

numero = int(input("Insira um número para saber se o mesmo é par: "))
if (numero % 2) == 0:
    print(f"{numero} é um número par")
elif (numero % 2) != 0:
    print(f"{numero} é um número impar")
