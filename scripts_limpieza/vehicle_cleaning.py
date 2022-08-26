import sys
import pandas as pd
import numpy as np
from call_api import api_to_df_upper_columns
from datetime import datetime
from datetime import date

df_vehicle_vehicle_crash = api_to_df_upper_columns('https://data.cityofnewyork.us/resource/bm4k-52h4.json')

#Convertiremos la fecha a un formato mas manejable
df_vehicle_vehicle_crash['CRASH_DATE'] = pd.to_datetime(df_vehicle_vehicle_crash['CRASH_DATE'].astype(str), format='%Y/%m/%d')

#Crearemos una nueva columna denominada 'WEEK_DAY'
df_vehicle_vehicle_crash['WEEK_DAY'] = df_vehicle_vehicle_crash['CRASH_DATE'].apply(date.isoweekday)

#Seleccionaremos y reordenaremos nuestro dataset
df_vehicle_vehicle_crash = df_vehicle_vehicle_crash[['COLLISION_ID','UNIQUE_ID', 'CRASH_DATE', 'CRASH_TIME', 'VEHICLE_ID', "STATE_REGISTRATION", 
                                                     "TRAVEL_DIRECTION", "DRIVER_SEX", "DRIVER_LICENSE_STATUS", "DRIVER_LICENSE_JURISDICTION", "PRE_CRASH", 
                                                     "PUBLIC_PROPERTY_DAMAGE", "CONTRIBUTING_FACTOR_1", "CONTRIBUTING_FACTOR_2"]]


#Reemplazando errores de tipeo
df_vehicle_vehicle_crash["CONTRIBUTING_FACTOR_1"].replace("Cell Phone (hand-Held)", "Cell Phone (hand-held)", inplace = True)
df_vehicle_vehicle_crash["CONTRIBUTING_FACTOR_1"].replace("Drugs (Illegal)", "Drugs (illegal)", inplace = True)
df_vehicle_vehicle_crash["CONTRIBUTING_FACTOR_1"].replace("Illnes", "Illness", inplace = True)

df_vehicle_vehicle_crash["CONTRIBUTING_FACTOR_2"].replace("Cell Phone (hand-Held)", "Cell Phone (hand-held)", inplace = True)
df_vehicle_vehicle_crash["CONTRIBUTING_FACTOR_2"].replace("Drugs (Illegal)", "Drugs (illegal)", inplace = True)
df_vehicle_vehicle_crash["CONTRIBUTING_FACTOR_2"].replace("Illnes", "Illness", inplace = True)

#Arreglando la columna "DRIVER_SEX"
df_vehicle_vehicle_crash["DRIVER_SEX"].replace("M", "Male", inplace = True)
df_vehicle_vehicle_crash["DRIVER_SEX"].replace("F", "Female", inplace = True)
df_vehicle_vehicle_crash["DRIVER_SEX"].replace("U", "Unknown", inplace = True)

#Reemplazando valores Nan de la columna "DRIVER_SEX"
df_vehicle_vehicle_crash["DRIVER_SEX"].fillna("Unknown", inplace = True)

#Reemplazando las direcciones por la palabra entera
df_vehicle_vehicle_crash["TRAVEL_DIRECTION"].replace("N", "North", inplace = True)
df_vehicle_vehicle_crash["TRAVEL_DIRECTION"].replace("S", "South", inplace = True)
df_vehicle_vehicle_crash["TRAVEL_DIRECTION"].replace("E", "East", inplace = True)
df_vehicle_vehicle_crash["TRAVEL_DIRECTION"].replace("W", "West", inplace = True)
df_vehicle_vehicle_crash["TRAVEL_DIRECTION"].replace("U", "Unknown", inplace = True)

df_vehicle_vehicle_crash["TRAVEL_DIRECTION"].replace("-", "Unknown", inplace = True)
df_vehicle_vehicle_crash["TRAVEL_DIRECTION"].fillna("Unknown", inplace = True)

#Reemplazando los valores Nan por "Unknown"
df_vehicle_vehicle_crash.STATE_REGISTRATION.fillna("Unknown", inplace = True)

#Reemplazando los valores Nan por "Unspecified"
df_vehicle_vehicle_crash.CONTRIBUTING_FACTOR_1.fillna("Unspecified", inplace = True)
df_vehicle_vehicle_crash.CONTRIBUTING_FACTOR_2.fillna("Unspecified", inplace = True)

#Reemplazando los valores Nan por "Unspecified"
df_vehicle_vehicle_crash.PUBLIC_PROPERTY_DAMAGE.fillna("Unspecified", inplace = True)

#Reemplazando los valores Nan por "Unknown"
df_vehicle_vehicle_crash.PRE_CRASH.fillna("Unknown", inplace = True)

#Reemplazando los valores Nan por "Unknown" en columna "DRIVER_LICENSE_JURISDICTION"
df_vehicle_vehicle_crash.DRIVER_LICENSE_JURISDICTION.fillna("Unknown", inplace = True)

#Reemplazando los valores Nan por "Unknown" en columna "DRIVER_LICENSE_STATUS"
df_vehicle_vehicle_crash.DRIVER_LICENSE_STATUS.fillna("Unknown", inplace = True)

#print(df_vehicle_vehicle_crash.head())

#Creando un nuevo dataframe
df_vehicle_vehicle_crash_clean = df_vehicle_vehicle_crash.copy()

#Guardando en un CSV
df_vehicle_vehicle_crash_clean.to_csv('vehicle_vehicle_crash_clean_prueba.csv', sep=',', index=False)

