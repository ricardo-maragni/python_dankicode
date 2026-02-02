"""
MINHA VERSÃO
"""

# Inicia o código
print("-" * 99)

print("Bem vindo(a) ao Supermercado Python!")

carrinho_de_compras = []

usuario = input("Qual é o seu nome? ")

qtd_itens = int(input(f"Ok {usuario}, quantos itens gostaria de comprar? "))

for x in range(qtd_itens):
    carrinho_de_compras.append(input("Digite aqui o produto que gostaria de comprar: "))

print(f"Os itens comprados foram: {carrinho_de_compras}")

# Finaliza o código
print("-" * 99)

"""
VERSÃO MELHORADA PELO CHATGPT

# Inicia o código
print("-" * 99)
print("Bem-vindo(a) ao Supermercado Python!")

carrinho_de_compras = []

usuario = input("Qual é o seu nome? ")

# Validação da quantidade de itens
while True:
    try:
        qtd_itens = int(input(f"Ok {usuario}, quantos itens gostaria de comprar? "))
        if qtd_itens < 0:
            print("Digite um número maior ou igual a zero.")
        else:
            break
    except ValueError:
        print("Por favor, digite apenas números.")

# Entrada dos produtos
for i in range(qtd_itens):
    produto = input(f"Digite o {i + 1}º produto que gostaria de comprar: ")
    carrinho_de_compras.append(produto)

# Saída formatada
print("\Os itens comprados foram:")
for i, item in enumerate(carrinho_de_compras, start=1):
    print(f"{i}. {item}")

# Finaliza o código
print("-" * 99)
"""
