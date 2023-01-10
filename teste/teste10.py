"""
EXERCICIO 01
Funções podem usar parâmetros para receber valores. Parâmetro é o nome da "variável" dentro dos parênteses, argumento é o valor passado para o parâmetro no momento da execução da função.

Sabendo disso, o código a seguir exibe o que na tela?"""

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)

"""
EXERCICIO 02

Quando falamos em argumentos, estamos falando sobre os valores passados para as funções no ato da sua execução. Existem argumentos nomeados e argumentos posicionais.

Argumentos nomeados recebem o nome do parâmetro antes do valor, argumentos posicionais recebem apenas o valor para preencher o parâmetro na ordem.

Por qual motivo você usaria argumentos nomeados?

a) é interresante usar argumentos nomeados para manter a ordem no envio de valores para a função

b) é interressante usar argumentos nomeados poder alterar a ordem no envio de valores para a função

c) é má prática de programação usar argumentos nomeados

d) Nenhuma opção
"""

'''
EXERCICIO 3

Escopo é algo muito usado na computação para delimitar e proteger determinadas partes do código. Em Python, o único escopo que vimos até então foi o escopo de funções (existem outros).

Ao definir variáveis e outros nomes dentro de escopo de funções em Python, é correto afirmar que:

a) Esses nomes não estarão disponiveis fora do  escopo da função (no escopo externo), mas estarão disponiveis em escopos mais interno(outras funçoes internas)

b) Esses nomes estarão disponiveis fora do escopo da função(no escopo externo), mas não estarão disponiveis em escopos mais internos (outras funções internas)

c) Esses nomes não estarão disponiveis fora do escopo da função (no escopo externo), também não estarão disponiveis em escopos mais internos (outras funções internas)

EXERCICIO 04

É possível alterar variáveis de escopo externo em escopo interno?

A) sim, com a palavra global
b) não

EXERCICIO 05 PRÁTICA

* crie uma função que mutiplica todos os argumento não nomeados recebidos
retorne o total para uma variavel e mostre o valor da variavel

* crie uma função fala se um numero é par ou impar 
retorne se o numero é par ou impar

* crie funções que duplicam, triplicam e quadruplicam o numero recebido com parametro
'''