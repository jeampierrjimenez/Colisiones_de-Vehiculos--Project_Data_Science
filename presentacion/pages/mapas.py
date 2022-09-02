import requests
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium
import folium
from folium import plugins
from folium.plugins import HeatMap


anio = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

mes = [6,1,2,3,4,5,7,8,9,10,11,12]

barrios = ('BRONX', 'BROOKLYN', 'STATEN ISLAND', 'MANHATTAN', 'QUEENS')


def mapa_anio_mes_barrio_api(año, mes, barrio):
  # Llamo a la api con los valores de la funcion y creo el df
  url = 'http://vps-2671696-x.dattaweb.com/collision/collisions_boro_year_month/' + barrio + '/' + str(año) + '/' + str(mes) + '/' 
  response = requests.get(url)
  df_json = pd.DataFrame(response.json()['data'])
  # Defino los limites del df a graficar
  df_grafico = df_json.loc[(df_json['latitude'] != '')&(df_json['longitude'] != '')&(df_json['latitude'].isna() != True)&(df_json['longitude'].isna() != True)]
  df_grafico['latitude'] = df_grafico['latitude'].astype(float)
  df_grafico['longitude'] = df_grafico['longitude'].astype(float)
  df_grafico = df_grafico.loc[(df_grafico['latitude']<=df_grafico['latitude'].median()+0.085)&(df_grafico['latitude']>=df_grafico['latitude'].median()-0.085)]
  df_grafico = df_grafico.loc[(df_grafico['longitude']<=df_grafico['longitude'].median()+0.085)&(df_grafico['longitude']>=df_grafico['longitude'].median()-0.085)]

  # Defino el mapa
  f = folium.Figure(width=700, height=700)
  m = folium.Map(width=500,height=500, location=[df_grafico['latitude'].median(),df_grafico['longitude'].median()], tiles = "Stamen Terrain", zoom_start = 11,use_container_width = True).add_to(f)
  calor = df_grafico[['latitude','longitude']]
  calor = calor.dropna(axis=0, subset=['latitude','longitude'])
  mapa_calor = [[row['latitude'],row['longitude']] for index, row in calor.iterrows()]
  HeatMap(mapa_calor, blur=18,radius=16,max_zoom=18).add_to(m)
  return m

def mapa_trafico_anio_mes_barrio_api(año, mes, barrio):
  # Llamo a la api con los valores de la funcion y creo el df
  url = 'http://vps-2671696-x.dattaweb.com/traffic/boro_year_month_alt/' + barrio + '/' + str(año) + '/' + str(mes) + '/' 
  response = requests.get(url)
  df_json = pd.DataFrame(response.json()['data'])
  # Defino los limites del df a graficar
  df_grafico = df_json.loc[(df_json['latitude'] != '')&(df_json['longitude'] != '')&(df_json['latitude'].isna() != True)&(df_json['longitude'].isna() != True)]
  df_grafico['latitude'] = df_grafico['latitude'].astype(float)
  df_grafico['longitude'] = df_grafico['longitude'].astype(float)
  # Defino el mapa
  f = folium.Figure(width=500, height=500)
  m = folium.Map(width=500,height=500, location=[df_grafico['latitude'].mean(),df_grafico['longitude'].mean()], tiles = "Stamen Terrain", zoom_start = 12).add_to(f)
  calor = df_grafico[['latitude','longitude']]
  calor = calor.dropna(axis=0, subset=['latitude','longitude'])
  mapa_calor = [[row['latitude'],row['longitude']] for index, row in calor.iterrows()]
  HeatMap(mapa_calor, blur=18,radius=16,max_zoom=18).add_to(m)

  return m


with st.sidebar:
    barrio1 = st.selectbox(
        'Barrio',
        barrios)
    anio1 = st.selectbox(
        'Año',
        anio)
    mes1 = st.selectbox(
        'Mes',
        mes)

tab1, tab2 = st.tabs(["Mapa de accidentes", "Mapa de volumen de trafico"])

with tab1:
    st.header('Accidentes')
    try:
        st_folium(mapa_anio_mes_barrio_api(anio1, mes1, barrio1), width=500, height=500)
    except:
        st.write('No hay datos que mostrar.')

with tab2:
    try:
        st_folium(mapa_trafico_anio_mes_barrio_api(anio1, mes1, barrio1), width=500, height=500)
    except:
        st.write('No hay datos que mostrar.')



