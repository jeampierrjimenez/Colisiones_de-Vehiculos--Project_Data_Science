import requests
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium
import folium
from folium import plugins
from folium.plugins import HeatMap
import geopandas as gpd
from shapely import wkt


anio = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]

mes = [1,2,3,4,5,6,7,8,9,10,11,12]

barrios = ['MANHATTAN', 'BROOKLYN', 'STATEN ISLAND', 'BRONX', 'QUEENS']


def mapa_anio_mes_barrio_api(año, mes, barrio):
  # Llamo a la api con los valores de la funcion y creo el df
  url = 'http://vps-2671696-x.dattaweb.com/collision/collisions_boro_year_month/' + barrio + '/' + str(año) + '/' + str(mes) + '/' 
  response = requests.get(url)
  df_json = pd.DataFrame(response.json()['data'])
  # Defino los limites del df a graficar
  df_grafico = df_json.loc[(df_json['latitude'] != '')&(df_json['longitude'] != '')&(df_json['latitude'].isna() != True)&(df_json['longitude'].isna() != True)]
  df_grafico['latitude'] = df_grafico['latitude'].astype(float)
  df_grafico['longitude'] = df_grafico['longitude'].astype(float)
  df_grafico = df_grafico.loc[(df_grafico['latitude']<=df_grafico['latitude'].median()+0.09)&(df_grafico['latitude']>=df_grafico['latitude'].median()-0.09)]
  df_grafico = df_grafico.loc[(df_grafico['longitude']<=df_grafico['longitude'].median()+0.09)&(df_grafico['longitude']>=df_grafico['longitude'].median()-0.09)]

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
  url = 'http://vps-2671696-x.dattaweb.com/traffic/boro_year_month/' + barrio + '/' + str(año) + '/' + str(mes) + '/' 
  response = requests.get(url)
  df_json = pd.DataFrame(response.json()['data'])

  # Trabajo las coordenadas
  df_json['Wkt_to_latlon'] = df_json['wktgeom'].apply(wkt.loads)
  gdf = gpd.GeoDataFrame(df_json, geometry='Wkt_to_latlon',crs='epsg:2263')
  # Cambio el formato
  gdf = gdf.to_crs(4326)
  df_json['latitude'] = gdf.geometry.y
  df_json['longitude'] = gdf.geometry.x
  df_json.head()

  # Defino los limites del df a graficar
  df_grafico = df_json.loc[(df_json['latitude'] != '')&(df_json['longitude'] != '')&(df_json['latitude'].isna() != True)&(df_json['longitude'].isna() != True)]
  df_grafico['latitude'] = df_grafico['latitude'].astype(float)
  df_grafico['longitude'] = df_grafico['longitude'].astype(float)
  # Defino el mapa
  f = folium.Figure(width=700, height=700)
  m = folium.Map(width=700,height=700, location=[df_grafico['latitude'].mean(),df_grafico['longitude'].mean()], tiles = "Stamen Terrain", zoom_start = 12).add_to(f)
  calor = df_grafico[['latitude','longitude']]
  calor = calor.dropna(axis=0, subset=['latitude','longitude'])
  mapa_calor = [[row['latitude'],row['longitude']] for index, row in calor.iterrows()]
  HeatMap(mapa_calor, blur=18,radius=16,max_zoom=18).add_to(m)

  return m




tab1, tab2 = st.tabs(["Mapa de accidentes", "Mapa de volumen de trafico"])


with st.sidebar:
    st.title('Colisiones a Personas')

    barrio = st.selectbox(
        'Barrio',
        barrios)
    anio = st.selectbox(
        'Año',
        anio)
    mes = st.selectbox(
        'Mes',
        mes)

with tab1:
    st.header('Accidentes')
    try:
        st_folium(mapa_anio_mes_barrio_api(anio, mes, barrio), width=900, height=900)
    except:
        st.write('No hay datos que mostrar.')

with tab2:
    st.header('Trafico')
    try:
        st_folium(mapa_trafico_anio_mes_barrio_api(anio, mes, barrio), width=900, height=900)
    except:
        st.write('No hay datos que mostrar.')




