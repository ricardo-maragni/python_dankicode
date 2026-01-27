"""
Estruturas de repetição - loops

O break serve para quebrar uma repetição de acordo com alguma regra.
No exemplo abaixo para ativar o break foi utilizado um if com a condição que
ele quebra caso o a variável 'a' seja igual a 3.
"""

# Valor inicial
a = 0
print(f"Valor inicial: {a}")

# Acrescentar +1 até chegar em 5
while a <= 5:
    print(a <= 5)
    print(a)
    if a == 3:
        break
    a = a + 1

# Resultado final
print(f"Resultado final: {a}")
print(a <= 5)
