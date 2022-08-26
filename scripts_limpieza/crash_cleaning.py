import sys
import pandas as pd
import numpy as np
from call_api import api_to_df_upper_columns
from datetime import datetime
from datetime import date

df_vehicle_crash = api_to_df_upper_columns('https://data.cityofnewyork.us/resource/h9gi-nx95.json')


#Convertiremos la fecha a un formato mas manejable
df_vehicle_crash['CRASH_DATE'] = pd.to_datetime(df_vehicle_crash['CRASH_DATE'].astype(str), format='%Y/%m/%d')

#Creare una nueva columna denominada 'WEEK_DAY'
df_vehicle_crash['WEEK_DAY'] = df_vehicle_crash['CRASH_DATE'].apply(date.isoweekday)

#Seleccionaremos y reordenaremos nuestro dataset
df_vehicle_crash = df_vehicle_crash[[   
                                        'COLLISION_ID', 'CRASH_DATE', 'CRASH_TIME', 'WEEK_DAY', 'BOROUGH', 'ZIP_CODE', 'LATITUDE', 
                                        'LONGITUDE', 'ON_STREET_NAME', 'CROSS_STREET_NAME', 
                                        'OFF_STREET_NAME', 'NUMBER_OF_PERSONS_INJURED', 'NUMBER_OF_PERSONS_KILLED', 
                                        'NUMBER_OF_PEDESTRIANS_INJURED', 'NUMBER_OF_PEDESTRIANS_KILLED', 
                                        'NUMBER_OF_CYCLIST_INJURED', 'NUMBER_OF_CYCLIST_KILLED', 'NUMBER_OF_MOTORIST_INJURED',
                                        'NUMBER_OF_MOTORIST_KILLED', 'CONTRIBUTING_FACTOR_VEHICLE_1',
                                        'CONTRIBUTING_FACTOR_VEHICLE_2', 'CONTRIBUTING_FACTOR_VEHICLE_3',
                                        'CONTRIBUTING_FACTOR_VEHICLE_4', 'CONTRIBUTING_FACTOR_VEHICLE_5'
                                        
                                        ]]


#Reemplazar valores con su valor adecuado
df_vehicle_crash["CONTRIBUTING_FACTOR_VEHICLE_1"].replace("Illnes", "Illness", inplace = True)
df_vehicle_crash["CONTRIBUTING_FACTOR_VEHICLE_1"].replace("Cell Phone (hand-Held)", "Cell Phone (hand-held)", inplace = True)
df_vehicle_crash["CONTRIBUTING_FACTOR_VEHICLE_1"].replace("Drugs (Illegal)", "Drugs (illegal)", inplace = True)
df_vehicle_crash["CONTRIBUTING_FACTOR_VEHICLE_1"].replace("Reaction to Other Uninvolved Vehicle", "Reaction to Uninvolved Vehicle", inplace = True)

df_vehicle_crash["CONTRIBUTING_FACTOR_VEHICLE_2"].replace("Illnes", "Illness", inplace = True)
df_vehicle_crash["CONTRIBUTING_FACTOR_VEHICLE_2"].replace("Cell Phone (hand-Held)", "Cell Phone (hand-held)", inplace = True)
df_vehicle_crash["CONTRIBUTING_FACTOR_VEHICLE_2"].replace("Drugs (Illegal)", "Drugs (illegal)", inplace = True)
df_vehicle_crash["CONTRIBUTING_FACTOR_VEHICLE_2"].replace("Reaction to Other Uninvolved Vehicle", "Reaction to Uninvolved Vehicle", inplace = True)

df_vehicle_crash["CONTRIBUTING_FACTOR_VEHICLE_3"].replace("Illnes", "Illness", inplace = True)
df_vehicle_crash["CONTRIBUTING_FACTOR_VEHICLE_3"].replace("Cell Phone (hand-Held)", "Cell Phone (hand-held)", inplace = True)
df_vehicle_crash["CONTRIBUTING_FACTOR_VEHICLE_3"].replace("Drugs (Illegal)", "Drugs (illegal)", inplace = True)
df_vehicle_crash["CONTRIBUTING_FACTOR_VEHICLE_3"].replace("Reaction to Other Uninvolved Vehicle", "Reaction to Uninvolved Vehicle", inplace = True)

df_vehicle_crash["CONTRIBUTING_FACTOR_VEHICLE_4"].replace("Illnes", "Illness", inplace = True)
df_vehicle_crash["CONTRIBUTING_FACTOR_VEHICLE_4"].replace("Cell Phone (hand-Held)", "Cell Phone (hand-held)", inplace = True)
df_vehicle_crash["CONTRIBUTING_FACTOR_VEHICLE_4"].replace("Drugs (Illegal)", "Drugs (illegal)", inplace = True)
df_vehicle_crash["CONTRIBUTING_FACTOR_VEHICLE_4"].replace("Reaction to Other Uninvolved Vehicle", "Reaction to Uninvolved Vehicle", inplace = True)

df_vehicle_crash["CONTRIBUTING_FACTOR_VEHICLE_5"].replace("Illnes", "Illness", inplace = True)
df_vehicle_crash["CONTRIBUTING_FACTOR_VEHICLE_5"].replace("Cell Phone (hand-Held)", "Cell Phone (hand-held)", inplace = True)
df_vehicle_crash["CONTRIBUTING_FACTOR_VEHICLE_5"].replace("Drugs (Illegal)", "Drugs (illegal)", inplace = True)
df_vehicle_crash["CONTRIBUTING_FACTOR_VEHICLE_5"].replace("Reaction to Other Uninvolved Vehicle", "Reaction to Uninvolved Vehicle", inplace = True)

#print(df_vehicle_crash.head())


#Creando un nuevo dataframe
df_vehicle_crash_clean = df_vehicle_crash.copy()

#Guardando en un CSV
df_vehicle_crash_clean.to_csv('vehicle_crash_clean_prueba.csv', sep=',', index=False)
