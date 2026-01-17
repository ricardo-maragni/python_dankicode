print("ola")
print('ola')

w = "Curso de Python3"
print(w)

"""comentário"""

a = """ola,
este eh o curso de python
espero que goste"""

print(a)

#Métodos das Strings

b = " Ola Mundo "
print(b)
print(b.strip())

c = "Ola Mundo"
print(c.lower())

d = "ola mundo"
print(d.upper())

e = "Ola"
f = " Mundo"
g = e + " " + f
print(g)

#Exercício 1

Cliente = "Gabriel"
Quantidade = "01"
Livro = "Lógica de Programação"
ValorLivro = "79,30"
Vendedor = "Marcos"
ValorComissao = "30,00"

print(
"Olá, " + Cliente + " sua compra de " + Quantidade + " qtd do livro " + Livro + " por R$ " + ValorLivro + " foi efetuada com sucesso!. "
)

print(
"Olá, " + Vendedor + " você acaba de receber uma comissão de R$ " + ValorComissao + " pela compra realizada pelo(a) cliente " + Cliente
)

#Exercício 2

Autora = "Beatriz"
Titulo = "redes neurais"
Compartilhamentos = "32"

print("Olá, " + Autora + " seu post com o título " + Titulo + " gerou " + Compartilhamentos + " compartilhamentos.")