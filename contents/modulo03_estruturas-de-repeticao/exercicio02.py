"""
Programa para calcular somas de sequências com frações
Cada sequência possui uma regra diferente para numerador e denominador
"""

# ======================================================
# EXERCÍCIO 1
# S = 3/40 + 32/39 + 33/38 + 34/37 + ... + 340/1
# numerador: começa em 32 e aumenta de 1 em 1
# denominador: começa em 39 e diminui de 1 em 1
# ======================================================

soma1 = 0

numerador = 32
denominador = 39

while denominador >= 1:
    soma1 += numerador / denominador
    numerador += 1
    denominador -= 1

print("Soma 1 =", soma1)


# ======================================================
# EXERCÍCIO 2
# S = 480/2 + 475/3 + 470/4 + ... (20 primeiros termos)
# numerador: diminui de 5 em 5
# denominador: aumenta de 1 em 1
# ======================================================

soma2 = 0

numerador = 480
denominador = 2

for _ in range(20):
    soma2 += numerador / denominador
    numerador -= 5
    denominador += 1

print("Soma 2 =", soma2)


# ======================================================
# EXERCÍCIO 3
# S = 1/2 + 3/23 + 7/25 + 15/27 + 31/29 + ... (15 termos)
# numerador: soma dobra (2, 4, 8, 16...)
# denominador: aumenta de 2 em 2
# ======================================================

soma3 = 0

numerador = 1
denominador = 2
incremento = 2

for _ in range(15):
    soma3 += numerador / denominador
    numerador += incremento
    incremento *= 2
    denominador += 2

print("Soma 3 =", soma3)
