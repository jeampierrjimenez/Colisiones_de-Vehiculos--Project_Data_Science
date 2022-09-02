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
  df = df.loc[df['year'] == anio]
  df = df.sort_values('qty', ascending=False)
  fig = px.bar(df.head(), x = 'driver_license_jurisdiction', y='qty', color='driver_license_jurisdiction')
  return fig

#--------------------------------------------------------------------------Daño a la propiedad

# Funcion para crear df (hago una funcion porque hay q pasarle el año a la url)
def crear_df_danio(anio):
  url_damage = 'http://vps-2671696-x.dattaweb.com/collision/public_damage/'+ str(anio)
  response_damage = requests.get(url_damage)
  df_damage = pd.DataFrame(response_damage.json()['data'])
  return df_damage
# Funcion para graficar (usa la funcion anterior)
def grafico_daño_propiedad(anio):
  df = crear_df_danio(anio)
  df = df.sort_values('qty', ascending=False).head()
  fig = px.bar(df, x = 'crash_time', y='qty', color='crash_time')
  return fig

#-------------------------------------------------------------------------- STREAMLIT
with st.sidebar:
  anio = st.selectbox(
    'Elegir año',
    anios)


tab1, tab2, tab3 = st.tabs(['Factores que contribuyen a los accidentes', "Estados origen de las licencias por accidente", "Daño a la propiedad"])
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









