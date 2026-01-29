"""
Como achar o fatorial de um número

Exemplos de fatorial:

4! = 4 * 3 * 2 * 1
9! = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
"""

numero = int(input("Insira um número: "))

fatorial = 1

if numero < 0:
    print("Não existe fatorial de números negativos!")
elif numero == 0:
    print("O fatorial de 0 é igual a 1")
else:
    for x in range(1, numero + 1):
        fatorial = fatorial * x
print(f"O fatorial de {numero} é {fatorial}")
