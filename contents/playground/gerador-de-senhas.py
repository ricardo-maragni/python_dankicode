import secrets
import string

# Inicia o código
print("-" * 99)

print("Bem vindo(a) gerador de senhas!")

tamanho = int(input("Digite o tamanho da senha: "))

letras = string.ascii_letters
numeros = string.digits
especiais = "!@#$%&*?"

senha = [
    secrets.choice(letras),
    secrets.choice(numeros),
    secrets.choice(especiais)
]

todos = letras + numeros + especiais

senha += [secrets.choice(todos) for _ in range(tamanho - 3)]

secrets.SystemRandom().shuffle(senha)

senha_final = "".join(senha)
print(senha_final)

# Finaliza o código
print("-" * 99)
