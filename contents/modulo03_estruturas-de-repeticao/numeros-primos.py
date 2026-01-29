"""
Descobrir se um número é primo
"""

print(99 * "-")

numero = int(input("Insira um número para descobrir se o mesmo é primo: "))

if numero > 1:
    for x in range(2, numero):
        if(numero % x) == 0:
            print("Não é um número primo!")
            break
    else:
        print("É um número primo!")
else:
    print("Não existem números primos negativos!")

print(99 * "-")
