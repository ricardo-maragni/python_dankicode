# Conversão de reais para dólar

print("Converter reais para dólar")

real = input("Digite quantos reais você deseja converter: ")

cotacao_dolar = "0.19"  # Cotação feita em 21/01/2026

dolar = float(real) * float(cotacao_dolar)

print(f"Quantidade de reais inserida é equivalente à {dolar} dólares")
