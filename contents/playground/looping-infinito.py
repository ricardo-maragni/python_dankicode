velocidade = 0
volta = 0
while velocidade < 100:
    velocidade += 1
    print(velocidade)
    if velocidade == 100:
        velocidade = 0
        volta += 1
        print(f"{volta}ª volta")
