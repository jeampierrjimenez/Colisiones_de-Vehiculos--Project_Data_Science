'''
Este es el script de la pestaña en la que se muestran los graficos relacionados al dataset de los vehiculos involucrados en los accidentes.
Aca mismo se definen funciones para llamar a la api de los datos simplificados y se los usa para graficar la información de interes.

Las librerias que se usan son streamlit, pandas, plotly.expres y requests.
Los requests realizados son a la api: http://vps-2671696-x.dattaweb.com/swagger/

Dentro de cada función se detalla su utilidad y los parametreos que reciben. Este es el listado de las mismas:
grafico_para_factores, grafico_licencias_estados, crear_df_danio, grafico_daño_propiedad.
'''

import streamlit as st
import pandas as pd
import plotly.express as px
import requests

anios = [2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]

#-------------------------------------------------------------------------------Factores por genero
url_factores = 'http://vps-2671696-x.dattaweb.com/collision/factor_genere/'
response_factores = requests.get(url_factores)
df_factores = pd.DataFrame(response_factores.json()['data'])
df_factores_clean = df_factores.loc[df_factores['contributing_factor'] != 'Unspecified']
df_factores_clean.head()

def grafico_para_factores(df, anio, sexo):
  '''
  Parametros:
    df = Es el dataframe que recibe para realizar el grafico correspondiente. 
      Deberia pasarse el dataframe sacado de la variable url_factores ya que cumple con los features que utiliza la función.
    anio = Limita el dataframe a los que corresponden a ese año.
    sexo = Es un parametro que permite limitar el grafico por el parametro sexo del dataframe.
    
  Utilidad:
    Esta funcion, con los parametros anteriores, realiza un grafico que representa el top 5 de los factores que contribuyen a los accidentes.
    El parametro sexo quedo fijado para que la funcion represente a ambos pero se puede utilizar para realizar la distinción.
  '''
  df = df.loc[df['crash_year'] == anio]
  data_m = df.loc[df['driver_sex'] == 'Male'].sort_values('qty', ascending=False)
  data_f = df.loc[df['driver_sex'] == 'Female'].sort_values('qty', ascending=False)
  data_g = df.groupby('contributing_factor')['qty'].sum().reset_index().sort_values('qty', ascending=False)
  fig1 = px.bar(data_m.head(), x = 'contributing_factor', y='qty', color='contributing_factor')
  fig2 = px.bar(data_f.head(), x = 'contributing_factor', y='qty', color='contributing_factor')
  fig3 = px.bar(data_g.head(), x = 'contributing_factor', y='qty', color='contributing_factor')
  if sexo == 'Male':
    return fig1
  elif sexo == 'Female':
    return fig2
  else:
    return fig3

#---------------------------------------------------------------------------Licencias por estado
url_licences = 'http://vps-2671696-x.dattaweb.com/collision/licence_state/'
response_licences = requests.get(url_licences)
df_licences = pd.DataFrame(response_licences.json()['data'])
# Creo un df aparte sin los unknown porque son demasiados
df_licences_clean = df_licences.loc[df_licences['driver_license_jurisdiction'] != 'Unknown']

def grafico_licencias_estados(df, anio):
  '''
  Parametros:
    df = Es el dataframe que recibe para realizar el grafico correspondiente. 
      Deberia pasarse el dataframe sacado de la variable url_licences ya que cumple con los features que utiliza la función.
    anio = Limita el dataframe a los que corresponden a ese año.
    
  Utilidad:
    Esta funcion, con los parametros anteriores, realiza un grafico que representa el top 5 de los Estados 
    por los que fueron emitidas las licencias de los conductores que participaron en los accidentes. 
    Para esto limita el df segun el parametro anio y excluye las licencias de Nueva York, luego las ordena de forma descendente 
    y realiza un grafico de barras con las 5 mayores.
  '''
  df = df.loc[(df['year'] == anio)&(df['driver_license_jurisdiction'] != 'NY')]
  df = df.sort_values('qty', ascending=False)
  fig = px.bar(df.head(), x = 'driver_license_jurisdiction', y='qty', color='driver_license_jurisdiction')
  return fig

#--------------------------------------------------------------------------Daño a la propiedad

# Funcion para crear df (hago una funcion porque hay q pasarle el año a la url)
def crear_df_danio(anio):
  '''
  Parametros:
    anio = Limita el dataframe a los que corresponden a ese año.
    
  Utilidad:
    Esta funcion crea un dataframe en determinado año llamando a la url de la api con los datos simplificados.
  '''
  url_damage = 'http://vps-2671696-x.dattaweb.com/collision/public_damage/'+ str(anio)
  response_damage = requests.get(url_damage)
  df_damage = pd.DataFrame(response_damage.json()['data'])
  return df_damage


# Funcion para graficar (usa la funcion anterior)
def grafico_daño_propiedad(anio):
  '''
  Parametros:
    anio = Limita el dataframe a los que corresponden a ese año.
    
  Utilidad:
    Esta funcion, llama a la funcion 'crear_df_danio' y le pasa el parametro que recibe para crear un dataframe en ese año particular.
    Luego ordena los horarios en los que mayor daño a la propiedad se causó, para luego realizar un grafico de barras.
    Para esto limita el df segun el parametro anio y excluye las licencias de Nueva York, luego las ordena de forma descendente y grafica con las 5 mayores.
  '''
  df = crear_df_danio(anio)
  df = df.sort_values('qty', ascending=False).head()
  fig = px.bar(df, x = 'crash_time', y='qty', color='crash_time')
  return fig

#-------------------------------------------------------------------------- STREAMLIT
with st.sidebar:
  anio = st.selectbox(
    'Elegir año',
    anios)


tab1, tab2, tab3 = st.tabs(['Factores que contribuyen a los accidentes', "Origen de las licencias por accidente", "Daño a la propiedad"])
with tab1:
  try:
    st.plotly_chart(grafico_para_factores(df_factores_clean, anio, 'Ambos'))
  except:
    st.write('No hay datos que mostrar.')
with tab2:
  try:
    st.plotly_chart(grafico_licencias_estados(df_licences_clean, anio))
  except:
    st.write('No hay datos que mostrar.')
with tab3:
  try:
    st.plotly_chart(grafico_daño_propiedad(anio))
  except:
    st.write('No hay datos que mostrar.')









