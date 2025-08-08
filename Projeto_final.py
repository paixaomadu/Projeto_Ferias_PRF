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

#Juntei todos os df para tranforar tudo em um df só
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

#Tranformação do df em csv
df_coli.to_csv("colisao_responsavel_por_mais_obitos.csv", index=False, sep=",", decimal=".")

#array de número de óbitos
array_coli= df_coli['contador']
dados_coli= np.array(array_coli)
dados_coli

#quartil
q1_coli= np.percentile(dados_coli, 25)
q1_coli

q2_coli= np.percentile(dados_coli, 50)
q2_coli

q3_coli= np.percentile(dados_coli, 75)
q3_coli

#Intervalo de interquartil
IQR= q3_coli - q1_coli

#limite superior
limite_superior_coli= q3_coli + (1.5 * IQR)
limite_superior_coli

#limite inferior
limite_inferior_coli= q1_coli - (1.5 * IQR)
limite_inferior_coli


#média da quantidade de óbitos 
media_coli= np.mean(dados_coli)
media_coli

#mediana da quantidade de óbitos 
mediana_coli= np.median(dados_coli)
mediana_coli

#distancia da quantidade de óbitos 
distancia_coli= (media_coli - mediana_coli) / mediana_coli *100
distancia_coli

#grafico outliers
plt.figure(figsize=(8, 5))
plt.boxplot(dados_coli, vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.axvline(limite_inferior_coli, color='red', linestyle='--', label=f"Limite Inferior ({limite_inferior_coli:.2f})")
plt.axvline(limite_superior_coli, color='red', linestyle='--', label=f"Limite Superior ({limite_superior_coli:.2f})")
plt.title("Colisão responsável por mais óbitos com delimitadores de outliers")
plt.xlabel("Quantidade de óbitos")
plt.legend()
plt.show()

#Gráfico matplot
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

#Tranformação do df em csv
dfvei.to_csv("veiculo_menos_seguro.csv", index=False, sep=",", decimal=".")

#array de veículo menos seguro para o condutor
array_vei= dfvei['contador']
dados_vei= np.array(array_vei)
dados_vei

#quartil
q1_vei= np.percentile(dados_vei, 25)
q1_vei

q2_vei= np.percentile(dados_vei, 50)
q2_vei

q3_vei= np.percentile(dados_vei, 75)
q3_vei

#Intervalo de interquartil
IQR= q3_vei - q1_vei

#limite superior
limite_superior_vei= q3_vei + (1.5 * IQR)
limite_superior_vei

#limite inferior
limite_inferior_vei= q1_vei - (1.5 * IQR)
limite_inferior_vei

#média da quantidade de óbitos por veículo
media_vei= np.mean(dados_vei)
media_vei

#mediana da quantidade de óbitos por veículo 
mediana_vei= np.median(dados_vei)
mediana_vei

#distancia da quantidade de óbitos por veículo 
distancia_vei= (media_vei - mediana_vei) / mediana_vei *100
distancia_vei

#grafico outliers
plt.figure(figsize=(8, 5))
plt.boxplot(dados_vei, vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.axvline(limite_inferior_vei, color='red', linestyle='--', label=f"Limite Inferior ({limite_inferior_vei:.2f})")
plt.axvline(limite_superior_vei, color='red', linestyle='--', label=f"Limite Superior ({limite_superior_vei:.2f})")
plt.title("Veículo menos seguro para o codutor com delimitadores de outliers")
plt.xlabel("Quantidade de óbitos")
plt.legend()
plt.show()

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

#Top 10 municípios que concentram os acidentes mais graves ------------------------------------------------------
df_graves= df_att.loc[(df_att['estado_fisico']== 'Lesões Graves')]
df_mun= df_graves.groupby(['estado_fisico','municipio'])['contador'].sum().reset_index()
df_mun10= df_mun.sort_values(by= 'contador', ascending= False). head(10)
df_mun10

#Tranformação do df em csv
df_mun.to_csv("mun_br_acidentes_graves.csv", index=False, sep=",", decimal=".")

#array de municípios
array_mun= df_mun['contador']
dados_mun= np.array(array_mun)
dados_mun

#quartil
q1_mun= np.percentile(dados_mun, 25)
q1_mun

q2_mun= np.percentile(dados_mun, 50)
q2_mun

q3_mun= np.percentile(dados_mun, 75)
q3_mun

#Intervalo de interquartil
IQR= q3_mun - q1_mun

#limite superior
limite_superior_mun= q3_mun + (1.5 * IQR)
limite_superior_mun

#limite inferior
limite_inferior_mun= q1_mun - (1.5 * IQR)
limite_inferior_mun

#média da quantidade de lesões graves por municipio
media_mun= np.mean(dados_mun)
media_mun

#mediana da quantidade de lesões graves por municipio
mediana_mun= np.median(dados_mun)
mediana_mun

#distancia da quantidade de lesões graves por municipio
distancia_mun= (media_mun - mediana_mun) / mediana_mun *100
distancia_mun

#grafico outliers
plt.figure(figsize=(8, 5))
plt.boxplot(dados_mun, vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.axvline(limite_inferior_mun, color='red', linestyle='--', label=f"Limite Inferior ({limite_inferior_mun:.2f})")
plt.axvline(limite_superior_mun, color='red', linestyle='--', label=f"Limite Superior ({limite_superior_mun:.2f})")
plt.title("Municípios com mais acidentes graves com delimitadores de outliers")
plt.xlabel("Quantidade de acidentes graves")
plt.legend()
plt.show()

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

#Tranformação do df em csv
df_del.to_csv("del_ocorrencia.csv", index=False, sep=",", decimal=".")

#array de delegacias
array_del= df_del['contador']
dados_del= np.array(array_del)
dados_del

#quartil
q1_del= np.percentile(dados_del, 25)
q1_del

q2_del= np.percentile(dados_del, 50)
q2_del

q3_del= np.percentile(dados_del, 75)
q3_del

#condição maior que 25%
df_25= df_del.loc[(df_del['contador'] >= q1_del)]
df_25= df_25[['delegacia', 'contador']]
df_25= df_25.sort_values(by= 'contador', ascending= False )
df_25

#Intervalo de interquartil
IQR= q3_del - q1_del

#limite superior
limite_superior_del= q3_del + (1.5 * IQR)
limite_superior_del

#limite inferior
limite_inferior_del= q1_del - (1.5 * IQR)
limite_inferior_del

#média das delegacias
media_del= np.mean(dados_del)
media_del

#mediana das delegacias
mediana_del= np.median(dados_del)
mediana_del

#distancia das delegacias
distancia_del= (media_del - mediana_del) / mediana_del *100
distancia_del

#grafico outliers
plt.figure(figsize=(8, 5))
plt.boxplot(dados_del, vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.axvline(limite_inferior_del, color='red', linestyle='--', label=f"Limite Inferior ({limite_inferior_del:.2f})")
plt.axvline(limite_superior_del, color='red', linestyle='--', label=f"Limite Superior ({limite_superior_del:.2f})")
plt.title("Delegacias com mais ocorrências com delimitadores de outliers")
plt.xlabel("Quantidade de ocorrências")
plt.legend()
plt.show()

#Tipo de acidente que mais ocorre por ano ------------------------------------------------------
tipo_acidente= df_att.groupby(['Ano', 'tipo_acidente'])['contador'].sum().reset_index()
acidente = tipo_acidente.groupby('Ano')['contador'].idxmax()
df_ano = tipo_acidente.loc[acidente].sort_values(by='Ano')
df_ano

#Tranformação do df em csv
df_ano.to_csv("tipo_acidente_ano.csv", index=False, sep=",", decimal=".")

#array do tipo de acidente que mais ocorre por ano
array_ano= df_ano['contador']
dados_ano= np.array(array_ano)
dados_ano

#média do tipo de acidente que mais ocorre por ano
media_ano= np.mean(dados_ano)
media_ano

#mediana do tipo de acidente que mais ocorre por ano
mediana_ano= np.median(dados_ano)
mediana_ano

#distancia do tipo de acidente que mais ocorre por ano
distancia_ano= (media_ano - mediana_ano) / mediana_ano *100
distancia_ano


#Evolução anual da quantidade de acidentes ------------------------------------------------------
df_evolucao= df_att.groupby('Ano')['contador'].sum().reset_index()
df_evolucao

#Tranformação do df em csv
df_evolucao.to_csv("evolucao_acidentes_ano.csv", index=False, sep=",", decimal=".")

#array da evolução
array_evolucao= df_evolucao['contador']
dados_evolucao= np.array(array_evolucao)
dados_evolucao

#quartil
q1_evolucao= np.percentile(dados_evolucao, 25)
q1_evolucao

q2_evolucao= np.percentile(dados_evolucao, 50)
q2_evolucao

q3_evolucao= np.percentile(dados_evolucao, 75)
q3_evolucao

#Intervalo de interquartil
IQR= q3_evolucao - q1_evolucao

#limite superior
limite_superior_evolucao= q3_evolucao + (1.5 * IQR)
limite_superior_evolucao

#limite inferior
limite_inferior_evolucao= q1_evolucao - (1.5 * IQR)
limite_inferior_evolucao

#média da evolução
media_evolucao= np.mean(dados_evolucao)
media_evolucao

#mediana da evolução
mediana_evolucao= np.median(dados_evolucao)
mediana_evolucao

#distancia da evolução
distancia_evolucao= (media_evolucao - mediana_evolucao) / mediana_evolucao *100
distancia_evolucao

#grafico outliers
plt.figure(figsize=(8, 5))
plt.boxplot(dados_evolucao, vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.axvline(limite_inferior_evolucao, color='red', linestyle='--', label=f"Limite Inferior ({limite_inferior_evolucao:.2f})")
plt.axvline(limite_superior_evolucao, color='red', linestyle='--', label=f"Limite Superior ({limite_superior_evolucao:.2f})")
plt.title("Evolução anual dos acidentes com delimitadores de outliers")
plt.xlabel("Quantidade de acidentes")
plt.legend()
plt.show()

#Gráfico da evolução
plt.plot(df_evolucao['Ano'],df_evolucao['contador'])
plt.title('\nEvolução da quantidade de acidentes por ano', fontsize=14)
plt.xlabel('\nAno\n')
plt.ylabel('\nNúmero de acidentes\n')
plt.grid(True)
plt.show
