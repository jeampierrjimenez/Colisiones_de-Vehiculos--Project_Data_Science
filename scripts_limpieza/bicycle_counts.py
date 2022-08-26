import sys
import pandas as pd
import numpy as np
from call_api import api_to_df_upper_columns
from call_api import api_to_df
from datetime import datetime
from datetime import date

#Data de Fuente "Bicycle Counts"
df_bicycle_counts = api_to_df('https://data.cityofnewyork.us/resource/uczf-rk3c.json')
df_bicycle_counts.sort_values("date", inplace = True)
df_bicycle_counts.reset_index(drop = True, inplace = True)

#Data de Fuente "Bicycle Counters"
df_bicycle_counts_info = api_to_df('https://data.cityofnewyork.us/resource/smn3-rzf9.json')

#Uniremos ambos dataframe para tener una tabla mas robusta
df_bicycle = pd.merge(df_bicycle_counts, df_bicycle_counts_info, on = "id", how = "left")

#Crearemos una nueva columna denominada 'WEEK_DAY'
df_bicycle['date'] = pd.to_datetime(df_bicycle['date'].astype(str), format='%Y/%m/%d')
df_bicycle['week_day'] = df_bicycle['date'].apply(date.isoweekday)

#Organizando y seleccionando columnas en nuestro dataset'
df_bicycle = df_bicycle[["countid", "id", "date", "week_day", "counts", "latitude", "longitude", "interval"]]

#print(df_bicycle.head())

#Creando un nuevo dataframe
df_bicycle_clean = df_bicycle.copy()

#Guardando en un CSV
df_bicycle_clean.to_csv('bicycle_clean_prueba.csv', sep=',', index=False)

