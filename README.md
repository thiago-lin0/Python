# Estudos de Python

---

# Sumário

### Sumário

1. [Objetivos](#objetivos)
2. [Comentários no Python](#comentários-no-python)
3. [Print e argumentos nomeados e não nomeados](#print-e-argumentos-nomeados-e-não-nomeados)
4. [Tipos de dados](#tipos-de-dados) 
    4.1. [Tipo String (str)](#string) 
    4.2. [Tipo inteito (int)](#int) 
    4.3. [Tipo Float](#float) 
    4.4. [Tipo Bollean (bool)](#bool)
5. [Typecasting ou conversão de tipos](#typecasting) 
    -[Convertendo floats em inteiros](#floats-int) 
    -[Convertendo String](#convertStrings) 
    -[Convertendo strings em números](#stringsNumeros)
6. [Exercicios](#exercicio)
7. [Variáveis](#var)
8. [Input e interação com o usuário](#input)
9. [Exercicios](#exerVar)
10. [Operadores aritimédicos](#oAritimedicos) 
    -[Concatenação (+) e repetição (\*) com operadores aritimédicos](#concat) 
    -[Precedência entre Operadores](#precedencia)
11. [Exercicio](#exercicioOpe)
12. [Operadores de Comparação](#opComparacao)
13. [Operadores de Atribuição](#OpAtribuicao)
14. [Operadores Lóficos](#OpLogicos)
15. [Estrutura de Condição](#condicao) 
    -[if/else](#ifelse) 
    -[if-elif-else](#ifelifelse)
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
    -[O while](#while) 
    -[Exercicio](#exercicio05)

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

EXERCICIO
pratique um pouco os exercicios de while faça o teste09.py
