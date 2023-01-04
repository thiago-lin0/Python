# Estudos de Python

********
### Sumário
1. [Objetivos](#objetivos)
2. [comentários no python](#coment)
3. [print e argumentos nomeados e não nomeados](#print)
4. [TIpos de dados](#types)
*******

<div id='objetivos'>

## Objetivos
  
Esse repositorio tem o intuito de estudos e deixar documentada para outras pessoas que queiram aprender python (e para mim caso me esqueça), esse Documento vai ter explicação e exercicios para podermo práticar juntos.

******
  
<div id='coment'>
  
## Comentários no Python
  
No python existem o documentário de uma linha usando a #, também esxite a docstring porém não é um comentário, mas caso você queira fazer um comentário de varias linhas, podemos usar ela, ''' seu comentário ''' ou """ seu comentario aqui """

EXEMPLOS
~~~~python
# Isso é um comentáio

'''
isso aqui é 
uma 
docstring
'''
~~~~

*******
  
<div id='print'>
 
## Print e argumentos nomeados e não nomeados
  print é uma função que recebe argumentos não nomeadoe e argumentos nomeados, argumentos nomeados é a passagem de valores fazendo associação com o nome do parâmetro e o valor que está sendo enviado já os não nomeado ou posicionais são utilizado para a passagem de valores onde cada valor estara na ordem conforme implementado na função.
  
EXEMPLO
 ~~~python
  #argumentos não nomeados
  print(12,34)
  
  '''
  quando vemos a saida dos argumentos ele já vem com espaço
  podemos modificar esse espaço com argumento nomeados sep=""
'''
  print(56,78, sep="-")
 ~~~~
 *******
 
 <div id='types'>
 
 ## Tipos de dados
 Nessa parte vamos falar sobre os diversos Tipos de Variáveis do Python. Independente se você vem de outra linguagem ou se está começando agora no Python, saber quais são e como utilizá-las é muito importante para desenvolvermos um código em Python. Vamos falar de alguns tipos nessa seção.
 
 ## Tipo String(str)
 É um conjunto de caracteres dispostos numa determinada ordem, geralmente utilizada para representar palavras, frases ou textos.
  
 EXEMPLOS:

  ~~~~python
nome = 'Thiago'
profissao = 'Engenheiro de Software'

print(type(profissao), profissao)
print(type(nome), nome)
   
SAIDA
<class 'str'> Engenheiro de Software
<class 'str'> Thiago

  ~~~~

## Tipo Inteiro (int)
O tipo inteiro é um tipo composto por caracteres numéricos (algarismos) inteiros.É um tipo usado para um número que pode ser escrito sem um componente decimal, podendo ter ou não sinal, isto é: ser positivo ou negativo.

Por exemplo, 21, 4, 0, e −2048 são números inteiros, enquanto 9.75, 1/2, 1.5 não são.

EXEMPLO
~~~~python
idade = 27
ano = 2023

print(type(idade))
print(type(ano))

SAIDA

<class 'int'> 27
<class 'int'> 2023
~~~~

## Ponto Flutuante ou Decimal (float)
É um tipo composto por caracteres numéricos (algarismo) decimais.O famoso ponto flutuante é um tipo usado para números racionais (números que podem ser representados por uma fração) informalmente conhecido como “número quebrado”.

>*OBS: Notem que o separador é o ponto e não a virgula

EXEMPLO

~~~~python
altura = 1.80
peso = 73.55

print(type(peso))
print(type(altura))


SAIDA

<class 'int'> 1.80
<class 'int'> 73.55


~~~~
