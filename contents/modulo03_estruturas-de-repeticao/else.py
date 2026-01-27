"""
Estruturas de repetição - loops

O 'else' dentro do 'while' serve colocar uma condição caso acontece algo além
da condição descrita no 'while'.
No exemplo abaixo é criado um 'while' para repetir até a atingir 5.
Aí quando atinge, é ativado o else.
"""

# Valor inicial
a = 0

while a <= 5:
    print(a <= 5)
    print(a)
    a = a + 1
else:
    print(f"a não é menor ou igual a 5. Valor de a: {a}")
