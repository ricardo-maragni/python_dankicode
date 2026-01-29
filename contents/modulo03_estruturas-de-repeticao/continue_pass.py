# ============================================
# Exemplo: diferença entre PASS e CONTINUE
# ============================================

print("=== Exemplo com PASS ===")

for numero in range(1, 6):

    # Quando o número for 3
    if numero == 3:
        # pass NÃO faz nada
        # o código continua normalmente
        pass

    # Este print será executado em TODOS os casos
    print(f"Número: {numero}")


print("\n=== Exemplo com CONTINUE ===")

for numero in range(1, 6):

    # Quando o número for 3
    if numero == 3:
        # continue PULA esta repetição do loop
        # tudo abaixo dele será ignorado
        continue

    # Este print NÃO será executado quando numero == 3
    print(f"Número: {numero}")


# ============================================
# Resumo mental:
#
# pass     -> não faz nada (apenas ocupa espaço)
# continue -> pula para a próxima repetição
# ============================================
