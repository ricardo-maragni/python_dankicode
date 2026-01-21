# Compra de produtos com percentual de desconto

print("Calcule o valor de um produto com desconto")

valor_inicial = input("Qual é o valor do produto (sem desconto)? ")

desconto_percentual = input("Será descontado qual percentual do produto? ")

desconto = float(valor_inicial) * (float(desconto_percentual)/100)

valor_final = float(valor_inicial) - float(desconto)

print(f"O valor final do produto é: {valor_final}")
