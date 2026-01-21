# Classificação de idade de um nadador

print("Bem vindo(a) ao Clube de Natação de Resende!")

idade = input("Qual é a sua idade? ")

if float(idade) < 16:
    print("Sua faixa etária é: MENOR")
elif float(idade) < 18:
    print("Sua faixa etária é: EMANCIPADO")
else:
    print("Sua faixa etária é: MAIOR")

if float(idade) < 5:
    print("Você ainda não pode se inscrever no clube!")
elif float(idade) < 7:
    print("Sua categoria será: Infatil A")
elif float(idade) < 10:
    print("Sua categoria será: Infatil B")
elif float(idade) < 13:
    print("Sua categoria será: Juvenil A")
elif float(idade) < 17:
    print("Sua categoria será: Juvenil B")
else:
    print("Só temos categorias para menores de 18 anos.")
