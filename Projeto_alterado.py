#Importação das bibliotecas -------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importação dos cvs (juntei os últimos 8 anos pois eram as bases que tinham) ------
df17= pd.read_csv('acidentes2017.csv', sep= ';', encoding="latin1")
df18= pd.read_csv('acidentes2018.csv', sep= ';', encoding="latin1")
df19= pd.read_csv('acidentes2019.csv', sep= ';', encoding="latin1")
df20= pd.read_csv('acidentes2020.csv', sep= ';', encoding="latin1") 
df21= pd.read_csv('acidentes2021.csv', sep= ';', encoding="latin1")
df22= pd.read_csv('acidentes2022.csv', sep= ';', encoding="latin1")
df23= pd.read_csv('acidentes2023.csv', sep= ';', encoding="latin1")
df24= pd.read_csv('acidentes2024.csv', sep= ';', encoding="latin1")
df25= pd.read_csv('acidentes2025.csv', sep= ';', encoding="latin1")

df= pd.concat([df17, df18, df19, df20, df21, df22, df23, df24, df25], ignore_index=True)
df

#Criei uma nova coluna só para o ano
df['data_inversa'] = pd.to_datetime(df['data_inversa'], format="%Y-%m-%d")
df['Ano'] = df['data_inversa'].dt.year

#Criei uma variável "contadora" para auxiliar no processo de contagem
df['contador']= 1
df

#Deixei somente as colunas que vou usar na análise para facilitar o processo
df_att= df[['data_inversa', 'municipio', 'dia_semana', 'delegacia', 'condicao_metereologica', 'tipo_veiculo', 'tipo_acidente', 'ordem_tipo_acidente','tipo_envolvido', 'estado_fisico', 'Ano', 'contador']]
df_att

#Qual colisão é responsável por mais óbitos? ------------------------------------------
dfobito= df_att.loc[(df_att['estado_fisico']== 'Óbito')]
df_coli= dfobito.groupby(['tipo_acidente', 'estado_fisico'])['contador'].sum().reset_index()
df_coli5= df_coli.sort_values(by= 'contador', ascending= False).head(5)
df_coli5

#array de número de óbitos
array= df_coli['contador']
dados= np.array(array)
dados

#média da quantidade de óbitos 
media= np.mean(dados)
media

#mediana da quantidade de óbitos 
mediana= np.median(dados)
mediana

#distancia da quantidade de óbitos 
distancia= (media - mediana) / mediana *100
distancia

#Gráfico
df_coli5.plot(kind= 'barh', x = 'tipo_acidente', y= 'contador')
plt.title('\nColisão responsável por maior número de óbitos\n')
plt.xlabel('\nNúmero de óbitos\n')
plt.ylabel('\nTipo de acidente\n')
plt.show

#Qual tipo de veículo é menos seguro para o condutor? ----------------------------------
dfvei= df_att.loc[(df_att['tipo_envolvido']== 'Condutor') & (df_att['estado_fisico']== 'Óbito')]
dfvei= dfvei.groupby(['tipo_veiculo', 'estado_fisico', 'tipo_envolvido'])['contador'].sum().reset_index()
dfvei5= dfvei.sort_values(by= 'contador', ascending= False).head(5)
dfvei

#array de veículo menos seguro para o condutor
array= dfvei['contador']
dados= np.array(array)
dados

#média da quantidade de óbitos por veículo
media= np.mean(dados)
media

#mediana da quantidade de óbitos por veículo 
mediana= np.median(dados)
mediana

#distancia da quantidade de óbitos por veículo 
distancia= (media - mediana) / mediana *100
distancia

#Gráfico
dfvei5.plot(kind= 'barh', x = 'tipo_veiculo', y= 'contador')
plt.title('\nVeículo menos seguro para o condutor\n')
plt.xlabel('\nNúmero de óbitos\n')
plt.ylabel('\nTipo de veículo\n')
plt.show

#Para ver a variação dos óbitos de motocicletas por ano
dfvei_ano= df_att.loc[(df_att['tipo_envolvido']== 'Condutor') & (df_att['estado_fisico']== 'Óbito')]
dfvei_ano= dfvei_ano.groupby(['Ano', 'tipo_veiculo', 'estado_fisico', 'tipo_envolvido'])['contador'].sum().reset_index()
ano = dfvei_ano.groupby('Ano')['contador'].idxmax()
df_por_ano = dfvei_ano.loc[ano].sort_values(by='Ano')
df_por_ano

#Top 10 municípios e rodovias que concentram os acidentes mais graves ------------------------------------------------------
df_graves= df_att.loc[(df_att['estado_fisico']== 'Lesões Graves')]
df_mun= df_graves.groupby(['estado_fisico','municipio'])['contador'].sum().reset_index()
df_mun10= df_mun.sort_values(by= 'contador', ascending= False). head(10)
df_mun10

#array de municípios
array= df_mun['contador']
dados= np.array(array)
dados

#média da quantidade de lesões graves por municipio
media= np.mean(dados)
media

#mediana da quantidade de lesões graves por municipio
mediana= np.median(dados)
mediana

#distancia da quantidade de lesões graves por municipio
distancia= (media - mediana) / mediana *100
distancia

#Gráfico do município
df_mun10.plot(kind= 'barh', x = 'municipio', y= 'contador')
plt.title('\nTop 10 municípios com maior concentração de acidentes graves\n')
plt.xlabel('\nNúmero de lesões graves\n')
plt.ylabel('\nMunicípio\n')
plt.show

#delegacias com 25% mais ocorrências ----------------------------------------------------------------
df_del= df_att.groupby('delegacia')['contador'].sum().reset_index()
df_del= df_del.sort_values(by= 'contador')
df_del

#array de delegacias
array= df_del['contador']
dados= np.array(array)
dados

#média das delegacias
media= np.mean(dados)
media

#mediana das delegacias
mediana= np.median(dados)
mediana

#distancia das delegacias
distancia= (media - mediana) / mediana *100
distancia

#Tipo de acidente que mais ocorre por ano ------------------------------------------------------
tipo_acidente= df_att.groupby(['Ano', 'tipo_acidente'])['contador'].sum().reset_index()
acidente = tipo_acidente.groupby('Ano')['contador'].idxmax()
df_ano = tipo_acidente.loc[acidente].sort_values(by='Ano')
df_ano

#array do tipo de acidente que mais ocorre por ano
array= df_ano['contador']
dados= np.array(array)
dados

#média do tipo de acidente que mais ocorre por ano
media= np.mean(dados)
media

#mediana do tipo de acidente que mais ocorre por ano
mediana= np.median(dados)
mediana

#distancia do tipo de acidente que mais ocorre por ano
distancia= (media - mediana) / mediana *100
distancia


#Evolução anual da quantidade de acidentes ------------------------------------------------------
df_evolucao= df_att.groupby('Ano')['contador'].sum().reset_index()
df_evolucao

#array da evolução
array= df_evolucao['contador']
dados= np.array(array)
dados

#média da evolução
media= np.mean(dados)
media

#mediana da evolução
mediana= np.median(dados)
mediana

#distancia da evolução
distancia= (media - mediana) / mediana *100
distancia

#Gráfico da evolução
plt.plot(df_evolucao['Ano'],df_evolucao['contador'])
plt.title('\nEvolução da quantidade de acidentes por ano', fontsize=14)
plt.xlabel('\nAno\n')
plt.ylabel('\nNúmero de acidentes\n')
plt.grid(True)
plt.show
