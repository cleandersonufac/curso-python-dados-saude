##############################abrindo banco de dados#############
df=pd.read_csv('SINASC_2024.csv',encoding='utf-8',sep=';')
df
# print(df.info())
# df=df[['contador','CODESTAB','CODMUNNASC','IDADEMAE','ESTCIVMAE','ESCMAE','QTDFILVIVO','QTDFILMORT'
#  ,'SEXO','PESO','RACACOR','IDADEPAI','QTDPARTNOR','QTDPARTCES','PARTO','DTNASC','GRAVIDEZ','GESTACAO','LOCNASC']]
# df
###################ou de forma simples#######################
df1 = df[df.columns[[0, 16, 2, 3,  5, 6, 7,9,10,18,22,21,42,40,41,14,13,12,4 ]]]
df1
# print(df1.info())
###############transformando coluna em datetime#######
df1['DTNASC'] = pd.to_datetime(df1['DTNASC'], format='%d%m%Y', errors='coerce')
df1
print(df1.info())
df1
#######################################################################
################ Mostrar as informações das variáveis #################
#######################################################################
#df1.info()# informações sobre os tipos de variáveis
#Mostrar o início (topo) da lista de dados
df1.head(20)
#Mostrar uma amostra aleatória de 10 linhas
df1.sample( 10 )
#Mostrar o fim (cauda) da lista de dados
df1.tail(10)
df1.dtypes # mostra os tipos de variáveis
df1.shape  # mostra a ordem do dataframe número de linhas e colunas
#df1.dropna()# Remover linhas com nulos
#df1.fillna(0)# Preencher nulos com 0
# df1['CODMUNNASC'] = df1['CODMUNNASC'].astype('float64')# mudar o tipo para float
# df1.info()
#######################################################################
###############excluir colunas e linhas do dataframe###################
#######################################################################
# axis = 1 para indicar uma coluna
dados = df1.drop(['DTNASC','CODMUNNASC'], axis=1)# axis = 1 para indicar uma coluna
dados
###########ou ####
dados= df1.drop(df1.columns[[1, 2]], axis=1)  # Exclui colunas 0, 1 e 2
dados
#axis = 0 para indicar uma linha
dados=df1.drop([0, 1, 6], axis=0)  # Exclui linhas 0, 1 e 6
dados
dados=df.drop([0, 1] + list(range(5,10,1)), axis=0)# Exclui linhas 0, 1 e uma lista 5:9
dados
#######################################################################
###############Acessar  colunas e linhas do dataframe###################
#######################################################################
# Acessar apenas uma coluna do dataframe
# coluna=df1['ORIGEM']
# print(coluna)
# # Acessar  mais de uma coluna do dataframe
# coluna=df[['ORIGEM','contador','CODMUNNASC']]
# print(coluna)
# Acessar apenas uma linha do dataframe
# linhas = df.iloc[1]
# print(linhas)
# Acessar linhas 1, 2, 3
# linhas = df.iloc[[1, 2, 5]]
# print(linhas)
#########################linhas e colunas##########################
# acessar a primeira, segunda e centésima linha das colunas 1, 2 e 99
print(df.iloc[[0, 1, 99],[0, 1 ,3]])# usar iloc
print(df.loc[[0, 1, 99],['DTNASC', 'IDADEMAE']])# usar loc ao invés de iloc
#######################################################################
################ Verificar se existem dados duplicados ################
#######################################################################
# Verificar se existem dados duplicados
# keep = False ==> mostra os duplicados
# keep = 'first' ==> mostra o 1º duplicado
# keep = 'last' ==> mostra o último duplicado
# Fazer uma busca por duplicados em alguma coluna específica
duplicados = df.duplicated(['IDADEMAE'], keep=False).sum()# mostra todas as linhas com pelos menos 2 linhas repetidas
# duplicados
# valores_unicos_duplicados = df[df.duplicated(['DTNASC'], keep=False)]['DTNASC'].nunique()
# print(f"Quantidade de valores únicos que se repetem: {valores_unicos_duplicados}")
#######################################################################
####### visualizando e contando as categorias de uma coluna ###########
#######################################################################
# Contando a quantidade de casos por categoria em uma variável
contar=df.SEXO.value_counts()
contar
# # # Contando a quantidade de casos por categoria em uma variável
contar=df['SEXO'].value_counts()
contar
contar=df.groupby(['SEXO']).size().reset_index(name='quantidade')
contar
# # # # # Contando a quantidade de casos por categoria em uma variável
# contar=df.groupby(['RACACOR']).size().reset_index(name='quantidade')
# contar
# # # Contando a quantidade de casos por categoria em mais de uma variável
contar=df.groupby(['RACACOR','ESTCIVMAE']).size().reset_index(name='quantidade')
print(contar)
###################################################################################
###visualizando e contando as categorias de uma coluna em tabela coloridas#########
###################################################################################
#########SEXO#######
###pip install jinja2 pandas 
#### import seaboarn as sns
#
#########
cm = sns.light_palette("green", as_cmap=True)
tabela = contar.style.background_gradient(cmap=cm, subset=['quantidade'])
tabela
#######################################################################
#####################tratamentos de valores ausentes###################
#######################################################################
# # Contar a quantidade de casos ausentes em cada variável
df.isnull().sum()# banco original
# Remove uma linha se PELO MENOS UM valor for nulo (NaN) nessa linha
# dados_sem_nulos = df.dropna(how = 'any' )
# dados_sem_nulos
##Contar a quantidade de casos ausentes em cada variável
# dados_sem_nulos.isnull().sum()# banco alterado
# dados_sem_nulos
# Estratégia 2
# Remove uma linha apenas se TODOS os valores forem nulos (NaN) nessa linha
# dados_sem_linhas_vazias = df.dropna(how = 'all' )
# dados_sem_linhas_vazias







