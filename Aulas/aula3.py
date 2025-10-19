import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
#########################abrir banco de dados original##############################
df=pd.read_csv('SINASC_2024.csv',encoding='utf-8',sep=';')
#####################selecionar colunas que vamos trabalhar#########################
df1 = df[df.columns[[0, 16, 2, 3,  5, 6, 7,9,10,18,22,21,42,40,41,14,13,12,4 ]]]
df1
#######################mudar coluna DTNACN para datetime###########################
df1['DTNASC'] = pd.to_datetime(df1['DTNASC'], format='%d%m%Y', errors='coerce')
print(df1.info())# verificar se ta tudo ok
###################################################################################
######################################################################
###### Preencher os valores ausentes com a MEDIANA da variável########
######################################################################
ausentes=df1.isnull().sum()# verificando quais colunas tem NA
print(ausentes)
mediana=df1["IDADEMAE"].median()#calculando a mediana da idade da mae
print(mediana)
# # # # Preenche os nulos com a mediana
df1["IDADEMAE"].fillna(mediana, inplace= True )
print(df1.isnull().sum())
# Preencher os valores ausentes (NULL) com a MÉDIA da variável
# Calcular a média
media = df1["IDADEMAE"].mean()
media
media = np.mean(df1["IDADEMAE"])
media
# Preenche os nulos com a média
df1["IDADEMAE"].fillna(media, inplace= True )
df1
print(df1.isnull().sum())
######################################################################
###### Recodificar valores para que sejam considerados ausentes#######
######################################################################
# Neste exemplo a variável SEXO apresenta alguns casos com o valor
# Preencher com nulo (nan) o valor 0
df1.PESO.replace(0 , np.nan, inplace= True )# trocar 0 por nan
print(df1.isnull().sum())
#######################substituir Nan por 0##
# Preencher Nan por 0
df1.PESO.replace(np.nan , 0, inplace= True )
print(df1.isnull().sum())
contar=df1.groupby(['PESO']).size().reset_index(name='quantidade')# conferir 
# contar# VERIFICAR
######################################################################
###############################TRABALHANDO COM DATAS #################
######################################################################
########## quantidade de nascidos durante o ano, mes e dia#######
contagem_anos = df1['DTNASC'].dt.year.value_counts().sort_index()
print(contagem_anos)

df1['DTNASC'].dt.year.value_counts().sort_index().plot(kind='bar')
#df1['DTNASC'].dt.year.value_counts().sort_index()
df1['DTNASC']

# #########
contagem_meses = df1['DTNASC'].dt.month.value_counts().sort_index()
# # # print("\nContagem por mês:")
print(contagem_meses)
df1['DTNASC'].dt.month.value_counts().sort_index().plot(kind='bar')
plt.show()
# # # #########
contagem_dias = df1['DTNASC'].dt.day.value_counts().sort_index()
# # # print("\nContagem por dia do mês:")
print(contagem_dias)
df1['DTNASC'].dt.day.value_counts().sort_index().plot(kind='bar')
plt.show()


######################################################################
#################TRABALHANDO COM DIFERENÇAS DE DATAS #################
######################################################################
#pip install datetime
#import datetime 
# Exemplo de uso:
datas = ['2022-05-15','2023-05-16','2024-05-17','2025-05-18']
data = pd.to_datetime(datas,format='%Y-%m-%d')
dat=pd.DataFrame(data,columns=['datas'])
# #############ACRESCENTANDO COLUNAS AO DATA FRAME
dat['anos']=dat['datas'].dt.year # CRIANDO UMA COLUNA COM OS ANOS
dat['meses']=dat['datas'].dt.month # CRIANDO UMA COLUNA COMO OS MESES
dat['dias']=dat['datas'].dt.day # CRIANDO UMA COLUNA COM OS DIAS
# ##################CALCULANDO DIFERENÇAS DE MESES##
quantidade_dias = pd.date_range(start='2022-05-17', end='2023-05-17', freq='D')
print('Quantidade de dias entre as datas',len(quantidade_dias))
quantidade_meses = pd.date_range(start='2022-05-17', end='2023-05-17', freq='M')
print('Quantidade de meses entre as datas',len(quantidade_meses))
quantidade_anos = pd.date_range(start='2022-05-17', end='2023-05-17', freq='Y')
print('Quantidade de anos entre as datas',len(quantidade_anos))
######################################################################
##########################Seleção e filtro de dados  #################
######################################################################
df1.nlargest(15 , 'IDADEMAE' )# Filtrar os 5 maiores valores de uma coluna
df1.nsmallest(35 , 'IDADEMAE' )# Filtrar os 5 menores valores de uma coluna
menores = df[(df.IDADEMAE <= 8 )]# Selecionar um subconjunto (intervalo de dados)
menores
menores = df1[(df1.IDADEPAI <= 9 )]# Selecionar um subconjunto (intervalo de dados)
menores
menores_12 = df1[(df1.IDADEMAE <= 11 ) & (df.QTDFILVIVO == 2 )]# Selecionar um subconjunto
menores_12
adultos = df1[(df1.IDADEMAE >= 18 )]# Selecionar um subconjunto (intervalo de dados)
adultos
adultosF = df1[(df1.IDADEMAE >= 18 ) & (df1.PESO < 4000 )]# Selecionar um subconjunto
adultosF# PESO DA CRIANÇA
adultosM = df1[(df1.IDADEPAI >= 18 ) & (df1.SEXO == 'Masculino' )]# Selecionar um subconjunto
adultosM
casos2 = df1[(df1.IDADEPAI >= 18 ) & (df1.SEXO == 'Masculino' ) & (df1.IDADEMAE <=18)]# Selecionar um subconjunto
casos2
# ########################nominal###
adultosF = df1[(df1.IDADEMAE >= 18 ) & (df1.SEXO == 'Feminino' )]# Selecionar um subconjunto
adultosF# sexo da criança
CASOS = df1[(df1.IDADEPAI >= 30 ) & (df1.IDADEMAE <=11 )]# Selecionar um subconjunto
CASOS
# ##################################
df1['SEXO'].replace({1: 'Masculino', 2: 'Feminino',0:'Ignorado'}, inplace=True)
df1
extrair_nome = df1[df1.SEXO.str.contains('M')]# Criar um subconjunto que contenham parte do texto em uma variável
extrair_nome
resultado = df1[df1.SEXO.str.contains('^F.*ino$', regex=True)]# extrair palavra que começa com (Mas) e termina com (ino)
print(resultado)
######################################################################
#########Criação de novas variáveis e preenchimento com valores#######
######################################################################
# # criar uma nova variável e atribuir um valor 'qualquer'
df1.loc[ (df.PESO< 2500 ), 'BAIXO_PESO' ] = 'Sim'
df1
df1.loc[ (df.PESO>= 2500 ), 'BAIXO_PESO' ] = 'Não'
df1
###############ou de forma #####
df1['BAIXO_PESO'] = np.where(df['PESO'] < 2500, 'Sim', 'Não')
df1
############Mais de duas categorias###############
# condicoes = [df1['PESO'] < 1500,(df1['PESO'] >= 1500) & (df1['PESO'] < 2500),
# (df1['PESO'] >= 2500) & (df1['PESO'] < 4000),
# (df1['PESO'] >= 4000) & (df1['PESO'] < 5000),df1['PESO'] >= 5000]
# #######
valores = ['Muito Baixo', 'Baixo', 'Normal', 'Alto', 'Muito Alto']
# #######
# df1['categorias_pesos'] = np.select(condicoes, valores)


#################################################################################
######################################################################
####################### Recodificar categorias########################
######################################################################
#########################abrir banco de dados original##############################

# leitura dos pacotes
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

df=pd.read_csv('SINASC_2024.csv',encoding='utf-8',sep=';')
#####################selecionar colunas que vamos trabalhar#########################
df1 = df[df.columns[[0, 16, 2, 3,  5, 6, 7,9,10,18,22,21,42,40,41,14,13,12,4 ]]]
#######################mudar coluna DTNACN para datetime###########################
df1['DTNASC'] = pd.to_datetime(df1['DTNASC'], format='%d%m%Y', errors='coerce')
print(df1.isnull().sum())
print(df1.info())
####errors='coerce' usado para converter valores não numerico em NA caso tenha
#################################################################################
# Trocar números por conteúdo das categorias
#############VERIFICAR CATEGORIAS DA VARIÁVEL SEXO ANTES DA SUBSTITUIÇÃO###
## inplece=True # Modifica o DataFrame ORIGINAL
## inplece=False # Cria uma NOVA cópia do DataFrame
##Use inplace=True quando quiser modificar o objeto original permanentemente
##Use inplace=False quando quiser manter o original intacto e trabalhar com uma cópia
print(df1['SEXO'].unique())
df1

############várias ao mesmo tempo
df1['SEXO'].replace({1: 'Masculino', 2: 'Feminino',0:'Ignorado'}, inplace=True)
df1
print(df1['SEXO'].unique())
print(df1['SEXO'].value_counts())
contar=df.groupby(['SEXO']).size().reset_index(name='quantidade')# conferir 
contar
############VERIFICAR CATEGORIAS DA VARIÁVEL PARTO ANTES DA SUBSTITUIÇÃO###
print(df1['PARTO'].unique())
df1['PARTO'].replace({1: 'Varginal', 2: 'Cesário',9:'Ignorado'}, inplace=True)
print(df1['PARTO'])
print(df1['PARTO'].unique())# VER VALORES ÚNICOS
print(df1['PARTO'].value_counts())#CONTAR AS CATEGORIAS
print(df1['PARTO'].isnull().sum())
#############VERIFICAR CATEGORIAS DA VARIÁVEL GRAVIDEZ ANTES DA SUBSTITUIÇÃO###
print(df1['GRAVIDEZ'].unique())
df1['GRAVIDEZ'].replace({1: 'Única', 2: 'Dupla',3:'Tripla ou mais',9:'Ignorado'}, inplace=True)
print(df1['GRAVIDEZ'])
print(df1['GRAVIDEZ'].unique())# VER VALORES ÚNICOS
print(df1['GRAVIDEZ'].value_counts())#CONTAR AS CATEGORIAS
print(df1['GRAVIDEZ'].isnull().sum())
############VERIFICAR CATEGORIAS DA VARIÁVEL GESTAÇÃO ANTES DA SUBSTITUIÇÃO###
print(df1['GESTACAO'].unique())
df1['GESTACAO'].replace({1: 'Menos de 22 semanas', 2: 'De 22 a 27 semanas',
3:'De 28 a 31 semanas',4: 'De 32 a 36 semanas',5: 'De 37 a 41 semanas',6: 'De 42 semanas ou mais',9:'Ignorado'}, inplace=True)
print(df1['GESTACAO'])
print(df1['GESTACAO'].unique())# VER VALORES ÚNICOS
print(df1['GESTACAO'].value_counts())#CONTAR AS CATEGORIAS
print(df1['GESTACAO'].isnull().sum())

# variável local de nascimento
print(df1['LOCNASC'].unique())
df1['LOCNASC'].replace({1: 'Hospital', 
                        2: 'Outros estabelecimentos de saúde',
                        3:'Domicílio',
                        4:'Outros',
                        9:'Ignorado',
                        5:'Aldeia Indígena',}, 
                        inplace=True)
print(df1['LOCNASC'])

#######################SALVANDO BANCO DE DADOS###############
# dados=pd.read_csv('df1.csv',encoding='utf-8',sep=';')
# dados
# dados=pd.read_csv('dados.csv',encoding='utf-8',sep=';')
# dados





