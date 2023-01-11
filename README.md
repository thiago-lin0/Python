# Estudos de Python

---

# Sumário

### Sumário

1. [Objetivos](#objetivos)
2. [Comentários no Python](#comentários-no-python)
3. [Print e argumentos nomeados e não nomeados](#print-e-argumentos-nomeados-e-não-nomeados)
4. [Tipos de dados](#tipos-de-dados)
   - [Tipo String (str)](#string)
   - [Tipo inteito (int)](#int)
   - [Tipo Float](#float)
   - [Tipo Bollean (bool)](#bool)
5. [Typecasting ou conversão de tipos](#typecasting)
   - [Convertendo floats em inteiros](#floats-int)
   - [Convertendo String](#convertStrings)
   - [Convertendo strings em números](#stringsNumeros)
6. [Exercicios](#exercicio)
7. [Variáveis](#var)
8. [Input e interação com o usuário](#input)
9. [Exercicios](#exerVar)
10. [Operadores aritimédicos](#oAritimedicos)
    - [Concatenação (+) e repetição (\*) com operadores aritimédicos](#concat)
    - [Precedência entre Operadores](#precedencia)
11. [Exercicio](#exercicioOpe)
12. [Operadores de Comparação](#opComparacao)
13. [Operadores de Atribuição](#OpAtribuicao)
14. [Operadores Lóficos](#OpLogicos)
15. [Estrutura de Condição](#condicao)
    - [if/else](#ifelse)
    - [if-elif-else](#ifelifelse)
16. [Exercicios](#exercicio01)
17. [Operadores de Associação](#opAssociacao)
18. [Exercicios](#exercicios02)
19. [Formatação de strings com f-strings](#f-strings)
20. [Fatiamento de Strings](#fatiamentoStrings)
21. [Função len()](#funcaolen)
22. [Exercicios](#exercicio03)
23. [Try e Except](#tryExcept)
24. [Exercicio](#exercicio04)
25. [Estrutura de repetição](#estruturaDeRepeticao)
    - [O while](#while)
    - [Exercicio](#exercicio05)
    - [for in](#for)
26. [Tipo list](#list)

---

<div id='objetivos'>

## Objetivos

Esse repositorio tem o intuito de estudos e deixar documentada para outras pessoas que queiram aprender python (e para mim caso me esqueça), esse Documento vai ter explicação e exercicios para podermo práticar juntos.

---

<div id='comentários-no-python'>
  
## Comentários no Python
  
No python existem o documentário de uma linha usando a #, também esxite a docstring porém não é um comentário, mas caso você queira fazer um comentário de varias linhas, podemos usar ela, ''' seu comentário ''' ou """ seu comentario aqui """

EXEMPLOS

```python
# Isso é um comentáio

'''
isso aqui é
uma
docstring
'''
```

---

<div id='print-e-argumentos-nomeados-e-não-nomeados'>
 
## Print e argumentos nomeados e não nomeados

print é uma função que recebe argumentos não nomeadoe e argumentos nomeados, argumentos nomeados é a passagem de valores fazendo associação com o nome do parâmetro e o valor que está sendo enviado já os não nomeado ou posicionais são utilizado para a passagem de valores onde cada valor estara na ordem conforme implementado na função.

EXEMPLO

```python
 #argumentos não nomeados
 print(12,34)

 '''
 quando vemos a saida dos argumentos ele já vem com espaço
 podemos modificar esse espaço com argumento nomeados sep=""
'''
 print(56,78, sep="-")
```

---

 <div id='tipos-de-dados'>
 
## Tipos de dados

Nessa parte vamos falar sobre os diversos Tipos de Variáveis do Python. Independente se você vem de outra linguagem ou se está começando agora no Python, saber quais são e como utilizá-las é muito importante para desenvolvermos um código em Python. Vamos falar de alguns tipos nessa seção.

### Tipo String (str)

É um conjunto de caracteres dispostos numa determinada ordem, geralmente utilizada para representar palavras, frases ou textos.

EXEMPLOS:

```python
nome = 'Thiago'
profissao = 'Engenheiro de Software'

print(type(profissao), profissao)
print(type(nome), nome)

SAIDA
<class 'str'> Engenheiro de Software
<class 'str'> Thiago

```

### Tipo inteito (int)

O tipo inteiro é um tipo composto por caracteres numéricos (algarismos) inteiros.É um tipo usado para um número que pode ser escrito sem um componente decimal, podendo ter ou não sinal, isto é: ser positivo ou negativo.

Por exemplo, 21, 4, 0, e −2048 são números inteiros, enquanto 9.75, 1/2, 1.5 não são.

EXEMPLO

```python
idade = 27
ano = 2023

print(type(idade))
print(type(ano))

SAIDA

<class 'int'> 27
<class 'int'> 2023
```

### Tipo float

É um tipo composto por caracteres numéricos (algarismo) decimais.O famoso ponto flutuante é um tipo usado para números racionais (números que podem ser representados por uma fração) informalmente conhecido como “número quebrado”.

> \*OBS: Notem que o separador é o ponto e não a virgula

EXEMPLO

```python
altura = 1.80
peso = 73.55

print(type(peso))
print(type(altura))


SAIDA

<class 'flaot'> 1.80
<class 'flaot'> 73.55


```

### tipo boolean (bool)

Tipo de dado lógico que pode assumir apenas dois valores: falso ou verdadeiro (False ou True em Python).Na lógica computacional, podem ser considerados como 0 ou 1.

Exemplos:

```python
fim_de_semana = True
feriado = False

print(type(fim_de_semana))
print(type(feriado))

SAIDA

<class 'bool'> true
<class 'boll'> false
```

> - Esxistem outros tipos de dados no python porém vamos aprender um pouqinho mais para frente

---

 <div id='typescasting'>

## Conversão de tipos ou Typecasting

Em Python, existem dois tipos de dados numéricos: inteiros e números de ponto flutuante (float). Às vezes, ao trabalhar no código de outra pessoa, será necessário converter um inteiro para um float ou vice-versa. Em outros casos, você pode estar usando um inteiro quando o que realmente precisa é de um float. O Python possui métodos integrados para permitir a conversão de inteiros em floats e floats em inteiros.

O método float() do Python irá converter inteiros em floats. Para usar essa função, adicione um inteiro dentro dos parênteses:

```python
   float(57)

SAIDA
   57.0
```

> - Nada me impede de usar em uma variavel

     ~~~~python
     t = 57
     print(float(f))

     SAIDA
        57.0
     ~~~~

### Convertendo floats em inteiros

O Python também possui uma função integrada para converter floats em inteiros: int(). A função int() funciona de maneira semelhante à função float(): é possível adicionar um número de ponto flutuante dentro dos parênteses para convertê-lo em um inteiro:

```python
     print(int(390.8))

     SAIDA
        390
```

> - Ao converter os floats em inteiros com a função int(), o Python corta a casa decimal e os números do float que restam são usados para criar um inteiro. Embora talvez você queira arredondar 390,8 para 391, o Python não fará isso através da função int().

### Convertendo String

Uma string é uma sequência de um ou mais caracteres (letras, números ou símbolos). As strings são uma forma comum de dados em programas de computador. Muitas vezes, pode ser necessário converter strings em números e números em strings, especialmente quando estivermos incluindo dados gerados pelo usuário.

Podemos converter números em strings usando o método str(). Vamos passar um número ou uma variável dentro dos parênteses do método e então esse valor numérico será convertido em um valor de string.

Primeiro, vamos ver como converter inteiros. Para converter o inteiro 12 em um valor de string, passe o número 12 para o método str():

```python
 print(str(12))

   SAIDA
       '12'
```

### Convertendo strings em números

As strings podem ser convertidas em números usando os métodos int() e float(). Se sua string não tiver casas decimais, você provavelmente vai querer convertê-la em um número inteiro, usando o método int().

<div id='exercicio'>

## Exercicios

> - Apartir de agora vai ter exercicios tanto teoricos quanto práticos para podermos nos analisar se estamos aprendendo. então você já está apto a fazer os 3 primeiros teste

<div id='var'>

## Variáveis em Python

Variaveis são usadas para salvar algo na memoria do computador
PEP8: inicie variaveis com letras minusculas pode usar numeros e underline\_
O sinal de = é o operador de atribuição. ele é usado para
atribuir um valor a um nome(variavel)
uso: nome_variavel = expressao

```python
nome = 'Thiago'
idade = 28
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade)
print('É maior de idade ?' , maior_de_idade)
```

> - f strings

```python
name = 'Thiago Lino'
height = 1.80
weight = 130
imc = weight / (height ** 2)

print(f'{name} tem {height:.2f} de altura,')
print(f'pesa {weight} quilos e seu IMC é')
print(f'{imc:.2f}')
```

> - :.2f, serve para arrendondar o numero com 2 casas deciamis

<div id='input'>

## Input e interação com o usuário

Esse é um artifício muito comum em programação, quando precisamos que o usuário passe ao programa algum tipo de dado. Em Python, fazemos isso utilizando a função input(), que é literalmente ‘entrada’ em inglês.
A função input() recebe como parâmetro uma string que será mostrada como auxílio ao usuário, geralmente o informando que tipo de dado o programa está aguardando receber.

> - obs: o input em sim ele não faz nada é somente de leitura, porém podemos guardar ele dentro de uma váriavel

EXEMPLO

```python
valor1 = int(input('digite um numero: '))
valor2 = int(input('digite outro numero: '))

print(f'A soma dos Valores é: {valor1 + valor2}')
```

> - O input nos guardar uma string então caso peça ao usuario um tipo de dados númericos, você precisa converter-los

<div id='exerVar'>

## Exercicios Práticos

Chegou a hora de fazermos o nosso primeiro teste prático então vá la na pasta teste e faça o nosso teste04.py, caso você queira a resolução é só falar

<div id='oAritimedicos'>

## Operadores aritimédicos

Esses operadores são utilizados para criarmos expressões matemáticas comuns, como soma, subtração, multiplicação e divisão.

Veja quais estão disponíveis no Python:

| Operador | Nome                      |
| -------- | ------------------------- |
| +        | Adição                    |
| -        | Subtração                 |
| \*       | Multiplicação             |
| /        | Divisão                   |
| //       | Divisão inteira           |
| %        | Resto da divisão (Módulo) |
| \*\*     | Exponenciação             |

EXEMPLOS

```python
quatro = 4
dois = 2

soma = quatro + dois
print(soma)  # Resultado: 6

subtracao = quatro - dois
print(subtracao)  # Resultado: 2

multiplicacao = quatro * dois
print(multiplicacao)  # Resultado: 8

divisao = quatro / dois
print(divisao)  # Resultado: 2.0

divisao_interna = quatro // dois
print(divisao_interna)  # Resultado: 2

modulo = quatro % dois
print(modulo)  # Resultado: 0

exponenciacao = quatro ** dois
print(exponenciacao)  # Resultado: 16

```

### Concatenação (+) e repetição (\_) com operadores aritimédicos

Também podemos unir ou concatenar letras com o sinal de (+), ou letras com números, já o operador (\*) quando multiplicado com uma string ele irá repetir essa str quantas vezes o numero que você multiplicou

### Precedência entre Operadores

A hierarquia vai da esquerda para direita

> (), \*_, _, /, + -

Os operadores com a mesma precedência são avaliados da esquerda para a direita

<div id='exercicioOpe'>

## Exercicios

Agora vá e teste seu conhecimento resolvendo o teste05.py

<div id='comparacao'>

## Operadores de Comparação

Como o nome já diz, esses Operadores são usados para comparar dois valores:

| Operador | Nome           | Função                                               |
| -------- | -------------- | ---------------------------------------------------- |
| ==       | igual a        | verifica se um valor é igual ao outro                |
| !=       | Diferente      | verifica se um valor é diferente do outro            |
| >        | Maior que      | verifica se um valor é maior do que o outro          |
| >=       | Maior ou igual | verifica se um valor é maior ou igual ao outro       |
| <        | Menor que      | verifica se um valor é menor do que o outro          |
| <=       | Menor ou igual | verifica se um valor é igual ou maior do que o outro |

EXEMPLOS

```python
var = 5

if var == 5:
    print('Os valores são iguais')

if var != 7:
    print('O valor não é igual a 7')

if var > 2:
    print('O valor da variável é maior de 2')

if var >= 5:
    print('O valor da variável é maior ou igual a 5')

if var < 7:
    print('O valor da variável é menor que 7')

if var <= 5:
    print('O valor da variável é menor ou igual a 5')

SAIDA
# Os valores são iguais
# O valor não é igual a 5
# O valor da variável é maior de 5
# O valor da variável é maior ou igual a 5
# O valor da variável é menor que 7
# O valor da variável é menor ou igual a 5

```

## Operadore de Atribuição

Esse Operadores são utilizados no momento da atribuição de valores à variáveis e controlam como a atribuição será realizada.

| Operador | Equivale   |
| -------- | ---------- |
| =        | x = 1      |
| +=       | x = x + 1  |
| -=       | x = x - 1  |
| \*=      | x = x \* 1 |
| /=       | x = x / 1  |
| %=       | x = x % 1  |

EXEMPLO

**Operador +=:**

```python
numero = 5
numero += 7
print(numero)  # Resultado será 10
```

---

**Operador -=:**

```python
numero = 5
numero -= 7
print(numero)  # Resultado será 2
```

---

**operador \*=**

```python
numero = 5
numero *= 2
print(numero)  # Resultado será 10
```

---

**operador /=**

```python
numero = 5
numero /= 4
print(numero)  # Resultado será 1.25
```

---

**operador %=**

```python
numero = 5
numero %= 2
print(numero)  # Resultado será 1
```

## Operdares Lógicos

Esses Operadores nos possibilitam construir um tipo de teste muito útil e muito utilizado em qualquer programa Python: os testes lógicos.

Python nos disponibiliza três tipos de Operadores Lógicos: o and, o or e o not.

Vamos ver mais sobre eles agora!

| Operador | Equivale                                                            |
| -------- | ------------------------------------------------------------------- |
| and      | Retorna true se todas as afirmações forem true v + v = v, v + f = f |
| or       | retorna true se uma das afirmações forem true v + f = v, v + v = v  |
| not      | retorna falso se o resultado verdadeiro                             |

EXEMPLO

```python
um1 = 7
num2 = 4

# Exemplo and
if num1 > 3 and num2 < 8:
    print("As Duas condições são verdadeiras")

# Exemplo or
if num1 > 4 or num2 <= 8:
    print("Uma ou duas das condições são verdadeiras")

# Exemplo not
if not (num1 < 30 and num2 < 8):
    print('Inverte o resultado da condição entre os parânteses')
```

## Estrutura de Condição

Agora que já está craque com os Operadores do Python, vamos aprender sobre nossa primeira estrutura condicional.

Sua sintaxe é bem simples, bastando utilizarmos if seguido pela condicao seguido por dois pontos:

EXEMPLO

```python
valor = 10

if valor > 5:
    print('O valor é maior que 5.')

    SAIDA
    # O valor é maior do que 5
```

> \*Neste caso, a condição está testando se o valor presente na variável valor é maior que 5. Caso seja true, a linha de código abaixo será executada (nesse exemplo, a chamada à função print()).

Caso você precise que um bloco de código que seja sempre executado, basta adicionar True à condição:

```python
if True:
    print("Este bloco sempre irá ser executado.")
```

### Estrutura Condicional if/else

Vimos na seção acima que o if executa um bloco de código se sua condição for atendida, mas e se ela não for atendida e você deseja realizar outra ação?
Bom, basta utilizarmos a estrutura condicional else!

Com ela, toda vez que uma condição não for atendida, o Python executará o bloco de código definido abaixo da cláusula else.

EXEMPLO

```python
idade = 20

if idade < 17:
    print('A idade é MENOR que 17')
else:
    print('A idade é MAIOR que 17')

    SAIDA
    A idade é MAIOR que 17
```

> - Neste caso, a condição testa se o valor da variável idade é menor que 17. Porém, como 17 é menor que 20, o bloco else é então executado, resultando em:

### Estrutura Condicional if-elif-else

O elif é utilizando quando mais de uma condição if precisa ser testada.

EXEMPLO

```python
linguagem = "Python"

if linguagem == "C++":
    print('C++ é uma linguagem de programação compilada.')
elif linguagem == "Python":
    print("Python é uma linguagem de programação de alto nível")
elif linguagem == "Java":
    print("Java é uma linguagem de programação amplamante utilizada no mercado")
else:
    print('Não é nenhuma das duas opções')

SAIDA
Python é uma linguagem de programação de alto nível

```

> Neste exemplo, estamos verificando o valor da variável linguagem em diversos testes. Note que a saída é exatamente o resultado da execução do elif, ja que a o valor da variável linguagem é igual à “Python”:

EXERCICIOS
Agora pare um momento e vá testar seus conhecimentos com os operadores que acabamos de estudar

## Operadores de Associação

Por último, temos os Operadores de Associação. Eles servem para verificar se determinado objeto está associado ou pertence a determinada estrutura de dados.

| Operador | Equivale                                                   |
| -------- | ---------------------------------------------------------- |
| in       | Retorna True caso o valor seja encontrado na sequência     |
| not in   | Retorna True caso o valor não seja encontrado na sequência |

EXEMPLOS

```python
lista = ["Python", 'Academy', "Operadores", 'Condições']

# Verifica se existe a string dentro da lista
print('Python' in lista)  # Saída: True

# Verifica se não existe a string dentro da lista
print('SQL' not in lista) # Saída: True
```

EXERCICIOS
agora faça o teste testeo7.md

## Formatação de strings com f-strings

F-strings foram criados para facilitar nossa vida e vieram para ficar! Também chamadas de “strings literais formatadas” (formatted string literals), f-strings são strings com a letra f no início e chaves {} para realizar a interpolação de expressões.

As expressões são processadas em tempo de execução e formatadas utilizadas o protocolo **format**.

EXEMPLOS

```python
nome = 'Monty Python'

print(f"Qual o melhor filme de comédia? {nome}!")

SAIDA
Qual o melhor Blog sobre Python? Monty Python!!!
```

**Utilizando funções**
Como f-strings são processadas em tempo de execução, podemos colocar quase todo tipo de código dentro das expressões.

EXEMPLO

```python
nome = 'monty python'

print(f"Qual o melhor filme de comedia? {nome.upper() + '!' * 3}")

SAIDA
Qual o melhor filme de comédia? MONTY PYTHON!!!

# OU AINDA

import math

x = 0.5

print(f'cos({x}) = {math.cos(x)}')

```

## Fatiamento de strings

Um segmento de uma string é chamado de fatia. Selecionar uma fatia é como selecionar um caractere:

```python
 s = 'Monty Python'
 s[0:5]

 SAIDA
'Monty'

s[6:12]

SAIDA
'Python'

```

O operador [n:m] retorna a parte da string do “enésimo” caractere ao “emésimo” caractere, incluindo o primeiro, mas excluindo o último. Este comportamento é contraintuitivo, porém pode ajudar a imaginar os índices que indicam a parte entre os caracteres.

![indices de fátia](https://pense-python.caravela.club/fig/tnkp_0801.png)

Se você omitir o primeiro índice (antes dos dois pontos), a fatia começa no início da string. Se omitir o segundo índice, a fatia vai ao fim da string:

```python
fruit = 'banana'

fruit[:3]
SAIDA
'ban'
fruit[3:]
SAIDA
'ana'
```

## Função len()

A função Len() existe para que possamos evitar de ter que ficar contando no dedo quantos itens tem uma lista ou quantas vezes aquele programa está entrando em um bloco de código. Ao utilizar essa função, é possível ter de imediato o resultado que precisamos.

```python
nome = 'Monty Python'
print(len(nome))

SAIDA
12
```

EXERCICIOS
Agora vamos da uma práticada, faça o exercicio teste08.py

## Try e Except

Em resumidas palavras o **try** é um bloco que permite testar um bloco de código para erros, já o \*\*except\*\* é o bloco que permite o manuseio do erro

Quando ocorre um erro ou exceção como o chamamos, o Python normalmente para e gerar uma mensagem de erro. Essas exceções podem ser tratadas usando o try declaração:

```python
try:
  print(x)
except:
  print("An exception occurred")

  # O try bloco irá gerar uma exceção, porque x não está definido:
```

> Como o bloco de tentativa gera um erro, o bloco de exceção será executado. Sem o bloco de tentativas, o programa travará e gerará um erro:

EXERCICIOS
tente fazer o teste09.py

## Estrutura de Repetição

O python exitem 2 estruturas de repetição o **while** e o **for**, agora iremos aprendor o while

### O loop While

Com o while, podemos executar um conjunto de instruções, desde que uma condição seja verdadeira.

```python
# imprima enquanto i for menor do que 6
i = 1 # acumulador
while i < 6: # condição
  print(i) # execução
  i += 1 # adicionando + 1 no acumulador
```

> _obs: lembre-se de incrementar i, caso contrário o loop continuará para sempre._

a declaração de break
Com o break, podemos parar o loop mesmo que while seja verdadeira:

EXEMPLO

```python
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
```

A declaração continue
Com o continue podemos parar o iteração atual e continuar para o próximo:

EXEMPLO

```python
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
```

#### EXERCICIO

pratique um pouco os exercicios de while faça o teste09.py

### Introdução ao for in

o for é usado para iterar uma sequência ( que é uma lista, uma tupla, um dicionário, um conjunto ou uma sequência ).

Isso é menos parecido com o for palavra-chave em outras linguagens de programação e funciona mais como um método iterador, conforme encontrado em outras linguagens de programação orientadas a objetos.

Com o for, podemos executar um conjunto de instruções, uma vez para cada item em uma lista, tupla, conjunto etc.

EXEMPLO

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

  SAIDA
  'apple'
  'bnana'
  'cherry'
```

O for não requer que uma variável de indexação seja definida previamente.

Até as strings são objetos iteráveis, elas contêm uma sequência de caracteres:

```python
for x in "banana":
  print(x)
```

### A declaração de break

Com o break podemos parar o loop antes de percorrer todos os itens:

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
```

### A declaração continue

Com o continue podemos parar o iteração atual do loop e continuar com o próximo:

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  # nao vai imorimir banana
```

### A função range()

Para percorrer um conjunto de códigos várias vezes, podemos usar o range( ),
O range( ) é uma função que retorna uma sequência de números, começando em 0 por padrão e incrementa em 1 ( por padrão ) e termina em um número especificado.

```python
for x in range(6):
  print(x)

  '''
  SAIDA
  0
  1
  2
  3
  4
  5
  '''
```

> O range( ) é padronizada como 0 como um valor inicial, no entanto, é possível especificar o valor inicial adicionando um parâmetro: intervalo ( 2, 6 ), que significa valores de 2 a 6 (, mas não incluindo 6 :

```python
for x in range(2, 6):
  print(x)

  '''
    SAIDA
    2
    3
    4
    5
  '''
```

> O range( ) por padrão função incrementa a sequência em 1, no entanto, é possível especificar o valor do incremento adicionando um terceiro parâmetro: range( 2, 30, 3):

```python
for x in range(2, 30, 3):
  print(x)

  '''
  SAIDA
  2
  5
  8
  11
  14
  17
  20
  23
  26
  29
  '''
```

### else no for loop

O else palavra-chave em um for loop especifica um bloco de código a ser executado quando o loop é concluído:

```python
for x in range(6):
  print(x)
else:
  print("Finally finished!")
```

> Nota: O bloco do else NÃO será executado se o loop for parado por um break declaração.

### Loops aninhados

Um loop aninhado é um loop dentro de um loop.
O "loop interno" será executado uma vez para cada iteração do "externo loop":

```python
adj = ["red", "big", "tasty"]
frutas = ["apple", "banana", "cherry"]

for x in adj:
  for y in frutas:
    print(x, y)
```

### Qual usar while ou o for?

Eles são laços de repetição e ambos fazem a mesma coisa, porem...

for: **é geralmente usado quando você sabe o número de iterações de antemão. Por exemplo para percorrer um array de 10 elementos**

while: **while é usado quando você tem uma idéia sobre a faixa de valores em que para fazer uma iteração, mas não sei o número exato de iterações que ocorrem.**

porem o for em bem mais rapido na execução segue o link
link: https://www.youtube.com/watch?v=aNsw0Bl8t6A

## Tipo List

As listas são usadas para armazenar vários itens em uma única variável.

As listas são um dos **4 tipos de dados internos** no Python usados para armazenar coleções de dados, e elas são mutaveis suporta vários valores de qualquer tipo

As listas são criadas usando colchetes:

```python
list = ["apple", "banana", "cherry"]
print(list)

'''
"apple", "banana", "cherry"
'''
```

### Itens da lista

Os itens da lista são interaveis e permitem valores duplicados.

Os itens da lista são indexados, o primeiro item tem índice [0], o segundo item tem índice [1] etc.

```python
#           0         1         2
list = ["apple", "banana", "cherry"]
```

### Itens de acesso

Os itens da lista são indexados e você pode acessá-los consultando o número do índice:

```python
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

'''
SAIDA
'apple'
'''
```

### Indexação negativa

Indexação negativa significa começar do final

-1 refere-se ao último item, -2 refere-se ao segundo último item etc.

```pyhton
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

'''
SAIDA
'cherry'
'''
```

### Gama de índices

Você pode especificar um intervalo de índices especificando por onde iniciar e por onde termine o intervalo.

Ao especificar um intervalo, o valor de retorno será uma nova lista com o itens especificados.

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

'''
SAIDA
"cherry", "orange", "kiwi"
'''
```

> Nota: A pesquisa começará no índice 2 ( incluído ) e terminará no índice 5 ( não incluído ).

Ao deixar de fora o valor inicial, o intervalo começará no primeiro item:

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

'''
SAIDA
"apple", "banana", "cherry", "orange"
'''
```

Ao deixar de fora o valor final, o intervalo continuará até o final da lista:

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

'''
SAIDA
"cherry", "orange", "kiwi", "melon", "mango"
'''
```

### Verifique se o item existe

Para determinar se um item especificado está presente em uma lista, use o in palavra-chave:

```python
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

  '''
  SAIDA
  "Yes, 'apple' is in the fruits list"
  '''
```

### Alterar valor do item

Para alterar o valor de um item específico, consulte o número do índice:

```python
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

'''
saida
"blackcurrant", "banana", "cherry"
'''
```

### Alterar uma faixa de valores de itens

Para alterar o valor dos itens dentro de um intervalo específico, defina uma lista com os novos valores e consulte o intervalo de números de índice em que deseja inserir os novos valores:

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

'''
SAIDA
"apple", "blackcurrant", "watermelon", "orange", "kiwi", "mango"
'''
```

### Inserir itens

Para inserir um novo item de lista, sem substituir nenhum dos valores existentes, podemos usar o insert().

O insert() é um metódo que insere um item no índice especificado:

```python
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

'''
SAIDA
"apple", "banana", "watermelon", "cherry"
'''
```

> Nota: Como resultado do exemplo acima, a lista agora conterá 4 itens.

### Inserindo um item no final da lista

com o metodo append() você consegue fazer esse feito

```python
thislist = ["apple", "banana", "cherry"]
thislist.append("watermelon")
print(thislist)

'''
SAIDA
"apple", "banana", "cherry","watermelon"
'''
```

### Remover item especificado

O remove() é um método remove o item especificado.

```python
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

'''
SAIDA
"apple", "cherry"
'''
```

### Remover índice especificado

O pop() é o método que remove o indice especificado.

```python
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

'''
SAIDA
"apple", "cherry"
'''
```

> Se você não especificar o índice, o pop() remove o último item.

```Python
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

'''
saida
"apple", "banana"
'''
```

O **del** palavra-chave também remove o índice especificado :

```python
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

'''
SAIDA
"banana", "cherry"
'''
```

> O del a palavra-chave também pode excluir a lista completamente.

```python
thislist = ["apple", "banana", "cherry"]
del thislist
```

### Limpando a lista

O clear() método esvazia a lista.

> A lista ainda permanece, mas não tem conteúdo.

```python
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

'''
SAIDA
[]
'''
```

### Concatendo Listas

temos duas formas de concatenar as listas a primeira que vamos ver é criando uma nova variavel

```python
listA = [0,1,2,3,4,5]
listB = [6,7,8,9,10]
listC = listA + listB
print(listC)
```

A outra forma é extendendo uma lista

```python
listA = [0,1,2,3,4,5]
listB = [6,7,8,9,10]
listA.extend(listB)
print(listA)
```

### Copiar uma lista

Você não pode copiar uma lista simplesmente digitando list2 = list1, porque: list2 será apenas um referência para list1, e alterações feitas em list1 será automaticamente também feito list2.

Existem maneiras de fazer uma cópia, uma maneira é usar a lista incorporada método copy().

```python
list = ["apple", "banana", "cherry"]
mylist = list.copy()
print(mylist)

'''
SAIDA
"apple", "banana", "cherry"
'''
```

> Outra maneira de fazer uma cópia é usar o método embutido list().

```python
frutas = ["apple", "banana", "cherry"]
mylist = list(frutas)
print(mylist)

'''
SAIDA
"apple", "banana", "cherry"
'''
```

### Faça um loop através de uma lista

Você pode percorrer os itens da lista usando um for loop:

```python
list = ["apple", "banana", "cherry"]
for x in list:
  print(x)

  '''
  SAIDA
  "apple",
  "banana",
  "cherry"
  '''
```

### Usando um loop while

Você pode percorrer os itens da lista usando um while loop.

Use o len() função para determinar o comprimento da lista, comece em 0 e percorra os itens da lista consultando os índices.

Lembre-se de aumentar o índice em 1 após cada iteração.

```python
list = ["apple", "banana", "cherry"]
i = 0
while i < len(list):
  print(thislist[i])
  i = i + 1
```

### Métodos de lista

| Metodo    | Descrição                                                                          |
| --------- | ---------------------------------------------------------------------------------- |
| append()  | Adiciona um elemento no final da lista                                             |
| clear()   | Remove todos os elementos da lista                                                 |
| copy()    | Retorna uma cópia da lista                                                         |
| count()   | Retorna o número de elementos com o valor especificado                             |
| extend()  | Adicionar os elementos de uma lista (ou qualquer iterável) ao final da lista atual |
| index()   | Retorna o índice do primeiro elemento com o valor especificado                     |
| insert()  | Adiciona um elemento na posição especificada                                       |
| remove()  | Remove o elemento na posição especificada                                          |
| reverse() | Inverte a ordem da lista                                                           |
| sort()    | Classifica a lista                                                                 |

### Introdução ao Desempacotamento + tuples (tuplas)

você tambêm pode transformar todos os dados de uma list em variaveis usando o desempacotamento

```python
nomes = ['Thiago', 'Marcos', 'Vitória'] #pacote
nome1, nome2, nome3 = nomes # Desempacotamentos
print(nome2)
# podemos fazer desse modo também
nome1, nome2, nome3 = ['Thiago', 'Marcos', 'Vitória']
print(nome2)
'''
SAIDA
'Marcos'
'Marcos'
'''
```

### desempacotando só um dado de uma list

```python
nome1, *resto = ['Thiago', 'Marcos', 'Vitória']
print(resto)

'''
SAIDA
['Marcos', 'Vitória']
'''
```

> desempacotei somente o primeiro index e empacotei de volta o resto da minha lista

certo,porem se eu quiser pegar o 2° termo da minha lista

```python
_, nome2, *resto = ['Thiago', 'Marcos', 'Vitória']
print(nome2)

'''
SAIDA
'Marcos'
'''
```

> caso você não vá usar os outros dados, por conveção colocamo \_(underline) para identificar que usaremos

## Tuple _(Tupla)_

As tuplas são usadas para armazenar vários itens em uma única variável.
diferente da lista a tuple é uma coleção encomendada e **imutável**.

```python
tuple = ("apple", "banana", "cherry")
print(tuple)

'''
SAIDA
("apple", "banana", "cherry")
'''
```

> Tudo que aprendemos sobre list serve também para as tuplas

> Oque você quiser fazer com uma lista mas não irá alterar a mesma, você pode utilizar uma tuple

> obs:. a lista é um pouco mais lenta que a list

### Convertendo uma lista em tuple

```python
nomes = ['Thiago', 'Marcos', 'Vitória']
nomes = tuple(nomes)
#posso fazer o inverso tambem
nomes = list(nomes)
```

## Enumerate()

Muitas vezes, ao lidar com iteradores, também precisamos manter uma contagem de iterações. O Python facilita a tarefa dos programadores ’, fornecendo uma função interna enenumerate( ) para esta tarefa. O método enumerate ( ) adiciona um contador a um iterável e o retorna na forma de enumerar objeto. Esse objeto enumerado pode ser usado diretamente para loops ou convertido em uma lista de tuplas usando o método list ( ).

### Sintaxe:

```python
enumerar ( iterável, iniciar = 0 )
```

Parâmetros:

- Iterável: qualquer objeto que suporte a iteração
- Iniciar: o valor do índice a partir do qual o contador deve ser iniciado, por padrão é 0

EXEMPLO

```python
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

obj1 = enumerate(l1)
obj2 = enumerate(s1)


print (list(enumerate(l1)))

print (list(enumerate(s1, 2)))

'''
SAIDA

[ ( 0, 'coma' ), ( 1, 'sono' ), ( 2, 'repita' ) ]
[ ( 2, 'g' ), ( 3, 'e' ), ( 4, 'e' ), ( 5, 'k' ) ]
'''
```

## Metódos útris para str _(string)_

### split e join

#### SPLIT

ele fatia uma string e coloca dentro de uma list

EXEMPLO

```python
frase = 'Olha só que, coisa interessante'
lista_de_palavra = frase.split()
print(lista_de_palavra)
lista_de_frase = frase.split(',') #podemos passar onde queremos dividir
print(lista_de_frase)

'''
SAIDA
['Olha', 'só', 'que,', 'coisa', 'interessante']
['Olha só que', ' coisa interessante']
'''
```

#### JOIN

une a string

EXEMPLO

```python
for i, frase in enumerate(lista_de_frase):
    print(lista_de_frase[i].strip())

frases_unidas = '-'.join(lista_de_palavra)

'''
SAIDA
Olha-só-que,-coisa-interessante
'''
```

## Operádor ternário no python

> <expressao1> if <condicao> else <expressao2>
> Primeiro, a condição é avaliada (ao invés de expressao1), se a condição for verdadeira, expressao1 é avaliada e seu valor é retornado; caso contrário, expressao2 é avaliada e seu valor retornado.

EXEMPLO

```python
x = 10
print ("par" if x % 2 == 0 else "impar")

'''
SAIDA
'par'
'''
```

> <condicao> and <expressao1> or <expressao2>
> No entanto, não funciona do mesmo modo que uma Expressão Condicional, se a condição for verdadeira, expressao1 é avaliada e seu valor retornado; se expressao1 for falso, expressao2 é avaliada e seu valor retornado.

```python
x = 10
print (x % 2 == 0 and "par" or "impar")

'''
SAIDA
'par'
'''
```

## Função em Python

Uma função é um bloco de código que só é executado quando é chamado. Você pode passar dados, conhecidos como parâmetros, para uma função.

Uma função pode retornar dados como resultado.

### Criando uma função

No Python, uma função é definida usando o **def** palavra-chave:

```python
def my_function():
  print("Hello from a function")
```

### Chamando uma função

Para chamar uma função, use o nome da função seguido por parênteses:

```python
def my_function():
  print("Hello from a function")

my_function() #chamando a função
```

### Argumentos

As informações podem ser passadas para funções como argumentos.

Os argumentos são especificados após o nome da função, dentro dos parênteses. Você pode adicionar quantos argumentos quiser, basta separá-los com uma vírgula.

O exemplo a seguir tem uma função com um argumento ( fname ). Quando a função é chamada, passamos um primeiro nome, usado dentro da função para imprimir o nome completo:

```python
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

'''
SAIDA
"Emil Refsnes"
"Tobias Refsnes"
"Linus Refsnes"
'''
```

> Argumentos são frequentemente abreviados para args em documentações em Python.

### Parâmetros ou argumentos?

Os termos parâmetro e argumento pode ser usado para a mesma coisa: informações que são passadas para uma função.

> Do ponto de vista de uma função: Um parâmetro é a variável listada dentro dos parênteses na definição da função. Um argumento é o valor que é enviado para a função quando é chamado.

### Número de argumentos

Por padrão, uma função deve ser chamada com o número correto de argumentos. Significando que se sua função espera 2 argumentos, você deve chamar a função com 2 argumentos, não mais e não menos.

```python
def my_function(fname, lname): # parametro
  print(fname + " " + lname)

my_function("Emil", "Refsnes") # argumento
```

> Se você tentar chamar a função com 1 ou 3 argumentos, receberá um erro:

### Argumentos arbitrários, \* args

Se você não souber quantos argumentos serão passados para sua função, adicione um \* antes do nome do parâmetro na definição da função.

Dessa forma, a função receberá um tupla argumentos e pode acessar os itens de acordo:

```python
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

'''
SAIDA
'The youngest child is Linus'
'''
```

> Argumentos Arbitrários são frequentemente abreviados para \*args em documentações em Python.

### Argumentos de palavras-chave

Você também pode enviar argumentos com o nome dachave = valor sintaxe.

Desta forma, a ordem dos argumentos não importa.

```python
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
```

> A frase _Argumentos de palavras-chave_ são frequentemente abreviados para kwargs em documentações em Python.

### Argumentos arbitrários de palavras-chave, \*\* kwargs

Se você não souber quantos argumentos de palavra-chave serão passados para sua função, adicione dois asteriscos: \*\* antes do nome do parâmetro na definição da função.

Dessa forma, a função receberá um dicionário argumentos e pode acessar os itens de acordo:

```python
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
```

### Valor padrão do parâmetro

O exemplo a seguir mostra como usar um valor de parâmetro padrão.

Se chamarmos a função sem argumento, ela usa o valor padrão:

```python
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

'''
SAIDA
I am from Sweden
I am from India
I am from Norway
I am from Brazil
'''
```

### Passando uma lista como argumento

Você pode enviar qualquer tipo de argumento de dados para uma função ( string, número, lista, dicionário etc. ), e vai ser tratado como o mesmo tipo de dados dentro da função.

Por exemplo. se você enviar uma lista como argumento, ela ainda será uma lista quando atinge a função

```python
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
```

### Valores de retorno

Para permitir que uma função retorne um valor, use o return declaração:

```python
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

```

#### EXERCICOS

tente fazer o teste10.py, nele tem teorico e prático

## Tipo de dados Dict _(Dicionário)_

Os dicionários são usados para armazenar valores de dados em pares de chave: valor.

Um dicionário é uma coleção encomendada \*, alterável e não permita duplicatas.

Os dicionários são escritos com colchetes e têm chaves e valores:

```python
isso_e_um_dicionario = {
  "marca": "Ford",
  "modelo": "Mustang",
  "ano": 1964
}
print(isso_e_um_dicionario)
```

### Itens de dicionário

Os itens do dicionário são pedidos, alteráveis e não permitem duplicatas.

Os itens do dicionário são apresentados em pares de **chave: valor** e podem ser referidos por usando o nome da chave.

```python
isso_e_um_dicionario = {
  "marca": "Ford",
  "modelo": "Mustang",
  "ano": 1964
}
print(isso_e_um_dicionario["marca"]
```

### Ordenado ou Não Ordenado?

> A partir da versão 3.7 do Python, os dicionários são ordenado. No Python 3.6 e anterior, os dicionários são não ordenado.

Quando dizemos que os dicionários são pedidos, significa que os itens têm uma ordem definida e essa ordem não será alterada.

Não ordenado significa que os itens não tenha uma ordem definida, você não pode se referir a um item usando um índice.

### Alterável

Os dicionários são alteráveis, o que significa que podemos alterar, adicionar ou remover itens após o dicionário foi criado.

### Duplicatas não permitidas

Os dicionários não podem ter dois itens com a mesma chave:

```python
isso_e_um_dicionario = {
  "marca": "Ford",
  "modelo": "Mustang",
  "ano": 1964,
  "ano": 2020
}
print(isso_e_um_dicionario)
```

### Comprimento do dicionário

Para determinar quantos itens um dicionário possui, use o len() função:

```python
print(len(isso_e_um_dicionario))
```

### Itens de dicionário - tipos de dados

Os valores nos itens do dicionário podem ser de qualquer tipo de dados:

```python
isso_e_um_dicionario = {
  "marca": "Ford",
  "electrico": False,
  "ano": 1964,
  "cor": ["red", "white", "blue"]
}
```

### O dict( ) Construtor

Também é possível usar o dict( ) construtor para fazer um dicionário

```python
isso_e_um_dicionario = dict(name = "John", age = 36, country = "Norway")
print(isso_e_um_dicionario)
```

### Acessando itens do cicionário

Você pode acessar os itens de um dicionário consultando o nome da chave, dentro colchetes:

```python
dict = {
  "marcar": "Ford",
  "modelo": "Mustang",
  "ano": 1964
}
x = dict["modelo"]
print(x)
'''
SAIDA
Mustang
'''
```

**Há também um método chamado get() que lhe dará o mesmo resultado:**

```python
x = dict.get("model")
print(x)
'''
SAIDA
Mustang
'''
```

### Obter chaves

O keys() O método retornará uma lista de todas as chaves no dicionário.

```python
x = dict.keys()
print(x)
'''
SAIDA
dict_keys(['brand', 'model', 'year'])
'''
```

## adicionando chaves

Você pode adicionar uma nova chave e atribuindo um valor para ela passando o nome do dicionario em seguida os colchetes e dentro dele o nome da nova chave e atribuido um valor :

```python
car = {
"marca": "Ford",
"modelo": "Mustang",
"ano": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white" #add uma nova chave e atribuindo um novo valor

print(x) #after the change

```

### Obter valores

O values() O método retornará uma lista de todos os valores no dicionário.

```python
x = car.values()
```

### Obter itens

O items() o método retornará cada item em um dicionário, como tuplas em uma lista.

```python
x = car.items()
'''
SAIDA
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
'''
```

### Verifique se as principais existências

Para determinar se uma chave especificada está presente em um dicionário, use o in palavra-chave:

```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in car:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
```

### **Alterar items**

### Alterar valores

Você pode alterar o valor de um item específico consultando o nome da chave:

```python
carro = {
  "marca": "Ford",
  "modelo": "Mustang",
  "ano": 1964
}
car["year"] = 2018
```

### Atualizar dicionário

O **update()** método atualizará o dicionário com os itens fornecidos argumento.

O argumento deve ser um dicionário ou um objeto iterável com pares key: value.

```python
car = {
  "marca": "Ford",
  "modelo": "Mustang",
  "ano": 1964
}
car.update({"ano": 2020})
```

### Removendo itens

Existem vários métodos para remover itens de um dicionário:

O pop() método remove o item com o nome da chave especificada:

```python
car = {
  "marca": "Ford",
  "modelo": "Mustang",
  "ano": 1964
}
car.pop("modelo")
print(car)
```

O **del** palavra-chave remove o item com o especificado Nome chave:

```python
car = {
  "marca": "Ford",
  "modelo": "Mustang",
  "ano": 1964
}
del car["modelo"]
print(car)

'''
SAIDA
{'brand': 'Ford', 'year': 1964}
'''
```

> O del palavra-chave também pode excluir o dicionário completamente

O **clear()** método esvazia dicionário:

```python
car = {
  "marcar": "Ford",
  "modelo": "Mustang",
  "ano": 1964
}
car.clear()
print(car)
'''
SAIDA
{}
'''
```

## Loop Através de um Dicionário

Você pode percorrer um dicionário usando um for loop.

Ao percorrer um dicionário, o valor de retorno é o chaves de o dicionário, mas existem métodos para retornar o valores também.

> Imprima todos os nomes de chaves no dicionário, um por um:

```python
car = {
  "marcar": "Ford",
  "modelo": "Mustang",
  "ano": 1964
}

for x in car:
  print(x)

'''
SAIDA
marcar
modelo
ano
'''
```

> Imprimir tudo valores no dicionário, um por um:

```python
car = {
  "marcar": "Ford",
  "modelo": "Mustang",
  "ano": 1964
}

for x in car.values():
  print(x)

'''
SAIDA
marcar
modelo
ano
'''
```

> fazer um loop através de ambos chaves e valores, usando o items() método:

```python
for x, y in car.items():
  print(x, y)

'''
SAIDA

brand Ford
model Mustang
year 1964
'''
```

### Copiar um dicionário

Você não pode copiar um dicionário simplesmente digitando dict2 = dict1, porque: dict2 será apenas um referência para dict1, e alterações feitas em dict1 será automaticamente também feito dict2.

Existem maneiras de fazer uma cópia, uma maneira é usar o dicionário embutido método copy().

Faça uma cópia de um dicionário com o copy() método:

```python
car = {
  "marca": "Ford",
  "modelo": "Mustang",
  "ano": 1964
}
mydict = car.copy()
print(mydict)
```

> Outra maneira de fazer uma cópia é usar a função interna dict().

```python
car = {
  "marca": "Ford",
  "modelo": "Mustang",
  "ano": 1964
}
mydict = dict(car)
print(mydict)
```

### Dicionários aninhados

Um dicionário pode conter dicionários, isso é chamado de aninhado dicionários.

```python
# Crie um dicionário que contenha três dicionários:
minha_familia = {
  "crianca1" : {
    "nome" : "Emil",
    "ano_de_nascimento" : 2004
  },
  "crianca2" : {
    "nome" : "Tobias",
    "ano_de_nascimento" : 2007
  },
  "crianca3" : {
    "nome" : "Linus",
    "ano_de_nascimento" : 2011
  }
}
```

> Ou, se você quiser adicionar três dicionários em um novo dicionário:

```python
# Crie três dicionários e crie um dicionário que conterá o outros três dicionários:
crianca1 = {
  "name" : "Emil",
  "year" : 2004
}
crianca2 = {
  "name" : "Tobias",
  "year" : 2007
}
crianca3 = {
  "name" : "Linus",
  "year" : 2011
}

minha_familia = {
  "crianca1" : crianca1,
  "crianca2" : crianca2,
  "crianca3" : crianca3
}
```

### Métodos de dicionarios

| Metodo      | Descrição                                                                                               |
| ----------- | ------------------------------------------------------------------------------------------------------- |
| clear()     | Remove todos os elementos do dicionário                                                                 |
| copy()      | Retorna uma cópia do dicionário                                                                         |
| fromkeys()  | Retorna um dicionário com as chaves e valores especificados                                             |
| get()       | Retorna o valor da chave especificada                                                                   |
| items()     | Retorna uma lista contendo uma tupla para cada par chave-valor                                          |
| keys()      | Retorna uma lista contendo as chaves do dicionário                                                      |
| pop()       | Remove o elemento com a chave especificada                                                              |
| popitem()   | Remove o último par chave-valor inserido                                                                |
| setdefaut() | Retorna o valor da chave especificada. Se a chave não existir: insira a chave, com o valor especificado |
| update()    | Atualiza o dicionário com os pares de valores-chave especificados                                       |
| values()    | Retorna uma lista de todos os valores no dicionário                                                     |

## Introdução ao tipo set em python (conjuntos)

### Set

Os conjuntos são usados para armazenar vários itens em uma única variável.

O conjunto é um dos **4 tipos de dados internos no Python** usados para armazenar coleções de dados, os outros **3 são Lista, Tuple, e Dicionário**, todos com diferentes qualidades e uso.

Um conjunto é uma coleção que é não ordenado, imutável\*, e não indexado.

> - Nota: Definir itens são imutáveis, mas você pode remover itens e adicione novos itens.

Os conjuntos são escritos com colchetes.

```python
set = {"apple", "banana", "cherry"}
print(set)
```

> Nota: Os conjuntos não são ordenados, portanto você não pode ter certeza de qual peça que os itens aparecerão

### Definir itens

Os itens definidos não são ordenados, imutáveis e não permitem valores duplicados

### Não ordenado

Não ordenado significa que os itens em um conjunto não têm uma ordem definida.

Definir itens pode aparecer em uma ordem diferente toda vez que você os usa, e não pode ser referido por índice ou chave.

### imutáveis

Os itens definidos são imutáveis, o que significa que não podemos alterar os itens após a criação do conjunto.

> Depois que um conjunto é criado, você não pode alterar seus itens, mas pode remover itens e adicione novos itens.

### Duplicatas não permitidas

Os conjuntos não podem ter dois itens com o mesmo valor.

```python
set = {"apple", "banana", "cherry", "apple"}

print(set)

'''
SAIDA
{"banana", "cherry", "apple"}
'''
```

### Obter o comprimento de um conjunto

Para determinar quantos itens um conjunto possui, use o len() função.

```python
set = {"apple", "banana", "cherry"}

print(len(set))
'''
SAIDA
3
'''
```

### Definir itens - tipos de dados

Definir itens pode ser de qualquer tipo de dados:

```python
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
```

> Um conjunto pode conter diferentes tipos de dados:

```python
set1 = {"abc", 34, True, 40, "male"}
```

### O set() Construtor

Também é possível usar o set( ) construtor para fazer um conjunto.

```python
thisset = set(("apple", "banana", "cherry")) # observe os colchetes duplos
print(thisset)
```

### Itens de acesso

Você não pode acessar os itens em um conjunto consultando um índice ou uma chave.

Mas você pode percorrer os itens definidos usando um **for** loop ou perguntar se um valor especificado está presente em um conjunto, usando o **in** palavra-chave.

```python
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
```

```python
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
```

> Depois que um conjunto é criado, você não pode alterar seus itens, mas pode adicionar novos itens

### Adicionar itens

> Depois que um conjunto é criado, você não pode alterar seus itens, mas pode adicionar novos itens.

Para adicionar um item a um conjunto, use o add() método

```python
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
```

### Adicionar Conjuntos

Para adicionar itens de outro conjunto ao conjunto atual, use o update() método.

```python
fruits = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

fruits.update(tropical)

print(fruits)
```

### Adicionar qualquer iterável

O objeto update() método não tem para ser um conjunto, pode ser qualquer objeto iterável ( tuplas, listas, dicionários etc. ).

```python
fruits = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(fruits)
```

### Remover item

Para remover um item em um conjunto, use o remove(), ou o discard() método.

```python
fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")

print(fruits)
```

> Nota: Se o item a ser removido não existir, remove() levantará um erro.

```python
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
```

> Nota: Se o item a ser removido não existir, discard() NÃO vai levantar erro.

Você também pode usar o pop() método para remover um item, mas esse método removerá o último item. Lembre-se de que define não são ordenados, portanto você não saberá qual item foi removido.

O valor de retorno do pop() método é o item removido.

```python
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
```

> O clear() método esvazia o conjunto:

```python
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
```

> O del palavra-chave excluirá o conjunto completamente:

```python
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
```

### Itens de loop

Você pode percorrer os itens definidos usando um for loop:

> Faça um loop através do conjunto e imprima os valores:

```python
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
```

### Juntando dois conjuntos

Existem várias maneiras de ingressar em dois ou mais conjuntos no Python.

Você pode usar o union() método que retorna um novo conjunto contendo todos os itens dos dois conjuntos, ou o update() método que insere todos os itens de um conjunto em outro:

```python
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
```

```python
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
```

> Nota: Ambos union() e update() excluirá quaisquer itens duplicados.

### Mantenha APENAS os Duplicados

O intersection_update() O método manterá apenas os itens presentes nos dois conjuntos.

```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)
```

> O intersection() método retornará um novo set, que contém apenas os itens presentes nos dois conjuntos.

```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)
```

### Mantenha tudo, mas NÃO os duplicados

O symmetric_difference_update() método vai manter apenas os elementos que NÃO estão presentes nos dois conjuntos.

```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
```

> O symmetric_difference() método retornará um novo conjunto, que contém apenas os elementos que NÃO estão presentes nos dois conjuntos.

```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)
```
