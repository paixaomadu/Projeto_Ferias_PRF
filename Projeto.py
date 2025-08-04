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
df_coli= df_coli.sort_values(by= 'contador')
df_coli

#Qual tipo de veículo é menos seguro para o condutor? ----------------------------------
dfvei= df_att.loc[(df_att['tipo_envolvido']== 'Condutor') & (df_att['estado_fisico']== 'Óbito')]
dfvei= dfvei.groupby(['Ano', 'tipo_veiculo', 'estado_fisico', 'tipo_envolvido'])['contador'].sum().reset_index()
dfvei= dfvei.sort_values(by= 'contador')
dfvei

#Para ver a variação dos óbitos de motocicletas por ano
dfvei= df_att.loc[(df_att['tipo_envolvido']== 'Condutor') & (df_att['estado_fisico']== 'Óbito')]
dfvei= dfvei.groupby(['Ano', 'tipo_veiculo', 'estado_fisico', 'tipo_envolvido'])['contador'].sum().reset_index()
idx = dfvei.groupby('Ano')['contador'].idxmax()
df_por_ano = dfvei.loc[idx].sort_values(by='Ano')
df_por_ano

#Quais municípios e rodovias concentram os acidentes mais graves? -----------------------------
df_graves= df_att.loc[(df_att['estado_fisico']== 'Lesões Graves')]
df_mun= df_graves.groupby(['estado_fisico','municipio', 'br'])['contador'].sum().reset_index()
df_mun= df_mun.sort_values(by= 'contador'). tail(10)
df_mun

#delegacias com mais ocorrências ----------------------------------------------------------------
df_del= df_att.groupby('delegacia')['contador'].sum().reset_index()
df_del= df_del.sort_values(by= 'contador')
df_del

#Tipo de acidente que mais ocorre por ano ------------------------------------------------------
dfvariacao= df_att.groupby(['Ano', 'tipo_acidente'])['contador'].sum().reset_index()
idx = dfvariacao.groupby('Ano')['contador'].idxmax()
df_ano = dfvariacao.loc[idx].sort_values(by='Ano')
df_ano