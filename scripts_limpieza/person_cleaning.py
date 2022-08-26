import sys
import pandas as pd
import numpy as np
from call_api import api_to_df_upper_columns
from datetime import datetime
from datetime import date

df_vehicle_person_crash = api_to_df_upper_columns('https://data.cityofnewyork.us/resource/f55k-p6yu.json')

#Convertiremos la fecha a un formato mas manejable
df_vehicle_person_crash['CRASH_DATE'] = pd.to_datetime(df_vehicle_person_crash['CRASH_DATE'].astype(str), format='%Y/%m/%d')


#Seleccionando y reorganizando el dataset
df_vehicle_person_crash = df_vehicle_person_crash[[ 'COLLISION_ID', 'CRASH_DATE', 'CRASH_TIME',
                                                    'PERSON_TYPE', 'PERSON_INJURY', 'PERSON_AGE', 'POSITION_IN_VEHICLE',
                                                    'SAFETY_EQUIPMENT', 'PED_LOCATION', 'PED_ACTION', 'PED_ROLE', 'CONTRIBUTING_FACTOR_1', 'CONTRIBUTING_FACTOR_2', 'PERSON_SEX']]


#Solucionando problemas con la columna "PERSON_AGE"
edades = df_vehicle_person_crash.PERSON_AGE
#edades_clean = edades.apply(lambda row: row if (row >= '0') else (row * -1) )

df_vehicle_person_crash["PERSON_AGE"] = edades

#saco los NaN
edades.fillna("Unknown", inplace = True)

#relleno los NaN con "U" (Unknown)
df_vehicle_person_crash.PERSON_SEX.fillna("U", inplace = True)

#relleno los NaN con unspecified, el resto esta todo bien
df_vehicle_person_crash.CONTRIBUTING_FACTOR_1.fillna("Unspecified", inplace = True)
df_vehicle_person_crash.CONTRIBUTING_FACTOR_2.fillna("Unspecified", inplace = True)

#relleno los NaN con Unknown, el resto esta todo bien
df_vehicle_person_crash.PED_ROLE.fillna("Unknown", inplace = True)

#relleno los NaN con Unknown, el resto esta todo bien
df_vehicle_person_crash.PED_ACTION.fillna("Unknown", inplace = True)

#relleno los NaN con Unknown, el resto esta todo bien
df_vehicle_person_crash.PED_LOCATION.fillna("Unknown", inplace = True)

#Limpieza
df_vehicle_person_crash.POSITION_IN_VEHICLE.fillna("Unknown", inplace = True)
df_vehicle_person_crash["POSITION_IN_VEHICLE"].replace("If one person is seated on another person&apos;s lap", "If one person is seated on another person's lap", inplace = True)

# limpieza
df_vehicle_person_crash.SAFETY_EQUIPMENT.fillna("Unknown", inplace = True)
df_vehicle_person_crash["SAFETY_EQUIPMENT"].replace("-", "Unknown", inplace = True)

#print(df_vehicle_person_crash.head())

#Creando un nuevo dataframe
df_vehicle_person_crash_clean = df_vehicle_person_crash.copy()

#Guardando en un CSV
df_vehicle_person_crash_clean.to_csv('vehicle_person_crash_clean_prueba.csv', sep=',', index=False)
