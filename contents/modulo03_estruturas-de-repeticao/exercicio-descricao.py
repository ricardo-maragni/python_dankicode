# Geral

"""
Todos os exercícios possuem alguma repetição de lógica de forma que você pode utilizar laços de repetição para desenvolvê-los.
"""

# 01 - Escreva um programa que leia 5 valores e encontre o maior e o menor deles. Mostre o resultado.

"""
Análise:

Eu poderia supor que o menor fosse um número pequeno qualquer (ou que o maior fosse um número grande) ao invés de, inicialmente, supor que ele fosse o primeiro?
Resposta: Não!
Exemplo: Suponha que fosse atribuído à variável menor o valor -500 e que o usuário digitasse apenas valores maiores que -500 (exemplo: -10, -9, 0, 6, 7 e 450), se o valor armazenado na variável menor nunca for trocado, a suposição estaria incorreta - erro de lógica - pois o valor supostamente menor estaria fora do conjunto dos valores digitados e, portanto, válidos). O mesmo raciocínio vale para maior

Solução: Supor que as variáveis maior e menor assumam o valor do primeiro elemento digitado, fora da estrutura de repetição. Assim, no caso do menor elemento, ao comparar o valor atualmente armazenado nesta variável com os demais elementos digitados (do 2º em diante) ele poderá ser alterado (ou não, caso o menor de todos os valores digitados seja efetivamente o primeiro). De igual forma, o valor da variável maior poderá ser alterado, caso haja entre os números posteriormente digitados um valor maior que o considerado o maior até então.
"""

# 02 - Escreva um programa para calcular as somas:

"""
S = 3/40 + 32 /39 + 33 /38 + 34 /37 + 340/1
S = 480/2 + 475/22 + 470/23 + 465/24 + 460/25 + (20 primeiros termos)
S = 1/2 + 3/23 + 7/25 + 15/27 + 31/29 + (15 primeiros termos)

20 termos - significa que você deve fazer a soma dos 20 primeiros termos

exemplo: se o termo 1° é igual a 5 e a regra de soma é termo anterior + 2.

1° termo: 5
2° termo: 5 + 2 = 7
3° termo: 7 + 2 = 9
4° termo: 9 + 2 = 11

até o último termo solicitado.
No caso o vigésimo termo. 20°.
A dica é você separar a sua divisão em numerador e denominador e ver o quanto que aumenta ou diminui em cada um separadamente.
As vezes o numerador aumenta de 1 em 1 e o denominador ta aumentando de 3 em 3.
"""
