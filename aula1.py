###########instalar bibliotecas#############
# py -m pip install numpy
# py -m pip install pandas
# py -m pip install seaborn
# py -m pip install matplotlib
# py -m pip install sympy
############importar bibliotecas############
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns
import sympy as sy
############################################
##################################################################
##################### Variáveis e comentários ####################
##################################################################
x = 10 # Criar variáveis
print (x)# Mostrar o conteúdo
y = x + 30# Somar variáveis e números
y
lista = [ 20 , 18 , 48 , 62 ]# Criar listas de números, variáveis e textos
lista
lista[ 0 ]# Mostrar o conteúdo da 1ª posição da lista
lista[ 2 ]# Mostrar o conteúdo da 3ª posição da lista
soma = lista[ 0 ] + lista[ 1 ]# Somar o 1º com o 2º elemento da lista
print(soma)# Mostrar o resultado
max(lista)# As funções também podem ser usadas combinada com as listas
min(lista)
##################################################################
#####################Operações e funções aritméticas #############
##################################################################
valor = 50 + 30# Adição
print(valor)
valor = 50 - 30# Subtração
print(valor)
valor = 50 / 10# Divisão
print(valor)
valor = 30 % 4# Resto da Divisão 
print(valor)
valor = 30 // 4# Parte inteira da Divisão 
print(valor)
valor = 30 / 4# Divisão exata
print(valor)
valor = 3 * 2# Multiplicação
print(valor)
valor = 3 ** 2# Exponenciação
print(valor)
abs ( -15 )# Função para calcular o valor absoluto
x = pow( 2 , 3 )# Função para exponenciação
print(x)
raiz=(9)**(1/2)# Função para radiciação
print(raiz)
minimo = min(4 , 18 , 6 )# Função para valor mínimo de uma lista
print(minimo)
maximo = max(45 , 67 , 23)# Função para valor máximo de uma lista
print(maximo)
minimo = np.min([4 , 18 , 6 ])# Função para valor mínimo de uma lista
print(minimo)
###################################################################
###Operações e funções aritméticas usando bibliotecas #############
###################################################################
# Funções trigonométricas
# math.sin(math.pi/2)    # seno
# math.cos(0)            # cosseno
# math.exp(2)            # e² # Exponencial
# math.e                 # 2.718281... (base do ln)
# math.factorial(5)      # 5! = 120
# print(math.log(10))     # ln(10)
# print(math.sqrt(25))    # raiz quadrada
# print(math.pi)          # constante pi
# log10 = math.log10(100)  # 2.0
# print(log10)
# log2 = math.log2(8)  # 3.0pp
# print(log2)
##################################################################
##Operações com matrizes usando bibliotecas ######################
##################################################################
###########ordem de uma matriz
M=np.array([[1,2,3],[4,5,6]])
M
M2=np.array([[1,2,3],[4,5,6],[7,8,9]])
M2
print("Ordem de M :", M.shape) 
print("Ordem de M2 :", M2.shape) 
# # ##############matriz de zeros
Matriz_de_zeros= np.zeros((4, 4))
Matriz_de_zeros
# # # # ##############matriz de uns
Matriz_de_uns=np.ones((3, 3))
Matriz_de_uns
# # # # ##############matriz identidade
Matriz_identidade=np.eye(6)
Matriz_identidade
# # # # ##############matriz diagonal
Matriz_diagonal=np.diag([1, 2, 3,4])
Matriz_diagonal
# # # # ##############matriz aleatória
Matriz_aleatória=np.random.rand(3, 3)
Matriz_aleatória
# # # # ##############matriz triangula superior
Triangular_superior=np.triu([[1, 2,4], [3, 4,6],[1,2,3]])
Triangular_superior
# # # # ##############matriz triagular inferior
Triangular_inferior=np.tril([[1, 2,4], [3, 4,6],[1,2,3]])
Triangular_inferior
# ##########ADIÇÃO DE MATRIZES
# # sejam as matrizes
A = np.array([[2,1,0], 
[-1,2,3]])
A
B=np.array([[3,-1,1],[0,-2,3]])
C=A+B
print(C)
# ##########SUBTRAÇÃO DE MATRIZES
A = np.array([[2,1], 
[1,0],[-3,1]])
B=np.array([[10,40],[20,50],[30,60]])
S=A-B
S2=B-A
print(S)
print(S2)
# ###PRODUTO ESCALAR
A = np.array([[1,-2], 
[3,0]])
M=3*A
print(M)
###MULTIPLICAÇÃO DE MATRIZES
# usa @ na multiplicação
A = np.array([[2,-1,0], 
[1,2,-3]])
B = np.array([[1,1], 
[1,2],[1,3]])
M=A@B
print(M)
####SOMA DIRETA
A = np.array([[1,2,3]])
B = np.array([[6,7], [4,-1]])
# Criando a matriz de zeros para o bloco superior direito
top = np.hstack([A, np.zeros((1, 2))])
# Criando a matriz de zeros para o bloco inferior esquerdo
bottom = np.hstack([np.zeros((2, 3)), B])
# Concatenando para formar a soma direta
soma = np.vstack([top, bottom])
print("Soma direta A⊕B =",soma)
###PRODUTO DIRETO
# # produto direto
A = np.array([[1,0],[0,1]])
V= np.array([[1],[2],[3]])
K1 = np.kron(A, V)
K2=np.kron(V, A)
print("PRODUTO DIRETO =",K1)
print("PRODUTO DIRETO =",K2)
#####Potencia de matrizes
A = np.array([[1, 2], [3, 4]])
potencia = np.linalg.matrix_power(A, 3)
potencia
####Posto ou rank de uma matriz
A = np.array([[4,2,2],
[2,2,0],[2,0,2]])
# Calcula o posto (rank)
posto = np.linalg.matrix_rank(A)
####Inversa de matrizes não singulares
# ####### inversa de uma matriz
A=np.array([[1,2,1],[2,1,0],[1,1,1]])
inv_A = np.linalg.inv(A)
inv_A 
#####Auto valores e autovetores
A=np.array([[3,1,1],[1,3,1],[1,1,3]])
autovalores, autovetores = np.linalg.eig(A)
print("auto valores de A",autovalores)
print("auto vetores de A",autovetores)
##################################################################
######################Operadores relacionais######################
##################################################################
# Operador de igualdade - comparando variáveis
x == y
# Operador de igualdade - comparando uma variável com um número
x == 20
# Operador de diferença
x != y
# Operador de maior
x > y
# Operador de menor
x < y
# Operador de maior ou igual
x >= y
# Operador de menor ou igual
x <= y
##################################################################
######################Variáveis do tipo texto#####################
##################################################################
# Criar variáveis do tipo texto (string)
nome = 'Juliano'
# Mostrar
print (nome)
# Variáveis de texto
sobrenome = 'Gaspar'
y = 20 # idade
# Mostrar duas variáveis
print (nome, sobrenome)
# Mostrar combinações de textos e variáveis de textos
print ( 'Nome do professor:' , nome, sobrenome)
# Mostrar texto e variáveis numéricas
print ( 'Idade:' , y)
#######################################################################
##################################################################
##########Importando dados para o DataFrames######################
##################################################################
df=pd.read_csv('magalhaes.csv',encoding='utf-8',sep=';')
#Ler os dados do arquivo e colocar os dados no objeto DataFrame
dados = pd.read_csv( 'pacientes.csv' )# Para ler os dados de um arquivo CSV
dados = pd.read_json( 'pacientes.json' )# Para ler os dados de um arquivo JSON
dados = pd.read_xml( 'pacientes.XML' )# Para ler os dados de um arquivo XML
dados = pd.read_excel( 'pacientes.xlsx' )# Para ler os dados de um arquivo Excel
# dados = pd.read_csv(arquivo, sep= ';' )# Importar o arquivo e forçar usar um separador específico (;)
# dados = pd.read_csv(arquivo, sep= ';' , skiprows= 1 )# Importar o arquivo e forçar usar um separador específico (;)
#linha (ou de um conjunto de linhas)(skiprows=1 é um parâmetro usado em bibliotecas de Python como Pandas
#usando para pular linha do datafrme
# dados = pd.read_csv(arquivo, sep= ';' , skiprows= 1 , encoding= 'latin1' )# Codificações comuns = latin1 / utf8 / cp1252
# dados = pd.read_csv(arquivo, usecols=[ 0 , 1 , 2 ])# Importar o arquivo e ler apenas algumas colunas
#############################
# (encoding='latin1') é um parâmetro usado em Python para especificar a codificação de caracteres ao 
# ler ou escrever arquivos de texto  com caracteres especiais (ç, ã, õ, é, ñ, etc.).
#############################
# (encoding='utf-8') é o padrão moderno e mais recomendado para codificação de 
# UTF-8 = Unicode Transformation Format - 8 bits
# Suporta praticamente todos os caracteres do mundo
# Padrão universal que inclui: português, espanhol, chinês, árabe, emojis, etc.
# Resumindo: UTF-8 é o método que permite seu computador mostrar corretamente textos em português, 
# chinês, emojis - tudo ao mesmo tempo!
#############################