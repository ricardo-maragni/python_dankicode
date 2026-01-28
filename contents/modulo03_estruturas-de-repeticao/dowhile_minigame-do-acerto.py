"""
do while

Código para adivinhar um número
"""

"""
EXEMPLO 1:

palpite = 0
numero = 9

while palpite != numero:
    print("Qual é o número correto? ")
    palpite = int(input())

print("Parabéns você acertou!")
"""

"""
EXEMPLO 2:

palpite = 5
numero = 9

while bool(palpite) is True:
    print("Qual é o número correto? ")
    palpite = int(input())
    if palpite == numero:
        print("Parabéns você acertou!")
        break
    else:
        print("Você errou!")
else:
    print("Erro na aplicação")
"""

# EXEMPLO 3:

palpite = 0
numero = 9

while True:
    print("Qual é o número correto? ")
    palpite = int(input())
    if palpite == numero:
        print("Parabéns você acertou!")
        break
    else:
        print("Você errou!")
else:
    print("Erro na aplicação")
    print(bool(palpite))
