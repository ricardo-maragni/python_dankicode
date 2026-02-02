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
