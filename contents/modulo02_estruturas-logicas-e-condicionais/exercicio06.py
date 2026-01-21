# Conversão de dólares para reais

print("Converter dólares para reais")

dolar = input("Digite quantos dólares você deseja converter: ")

cotacao_real = "5.33"  # Cotação feita em 21/01/2026

real = float(dolar) * float(cotacao_real)

print(f"Quantidade de dólares inserida é equivalente à {real} reais")
