import sys
import pandas as pd
import numpy as np
from call_api import api_to_df_upper_columns
from datetime import datetime
from datetime import date

df_traffic = api_to_df_upper_columns('https://data.cityofnewyork.us/resource/btm5-ppia.json')

#Convertiremos la fecha a un formato mas manejable
df_traffic['DATE'] = pd.to_datetime(df_traffic['DATE'].astype(str), format='%Y/%m/%d')

# renombramos la columna para que siga los nombres del resto
df_traffic.rename(columns = {"SEGMENTID": "SEGMENT_ID", 
                            '_12_00_1_00_AM':  "12:00-1:00AM", '_1_00_2_00AM': "1:00-2:00AM",
                            '_2_00_3_00AM': "2:00-3:00AM", '_3_00_4_00AM': "3:00-4:00AM",
                            '_4_00_5_00AM': "4:00-5:00AM", '_5_00_6_00AM': "5:00-6:00AM",
                            '_6_00_7_00AM': "6:00-7:00AM", '_7_00_8_00AM': "7:00-8:00AM",
                            '_8_00_9_00AM': "8:00-9:00AM", '_9_00_10_00AM': "9:00-10:00AM",
                            '_10_00_11_00AM': "10:00-11:00AM", '_11_00_12_00PM': "11:00-12:00PM",
                            '_12_00_1_00PM': "12:00-1:00PM", '_1_00_2_00PM': "1:00-2:00PM",
                            '_2_00_3_00PM': "2:00-3:00PM", '_3_00_4_00PM': "3:00-4:00PM",
                            '_4_00_5_00PM': "4:00-5:00PM", '_5_00_6_00PM': "5:00-6:00PM",
                            '_6_00_7_00PM': "6:00-7:00PM", '_7_00_8_00PM': "7:00-8:00PM",
                            '_8_00_9_00PM': "8:00-9:00PM", '_9_00_10_00PM': "9:00-10:00PM",
                            '_10_00_11_00PM': "10:00-11:00PM", '_11_00_12_00AM': "11:00-12:00AM"}, 
                            inplace = True)

#Completando los valores Nan con cero(0)
df_traffic["12:00-1:00AM"].fillna(0, inplace = True)
df_traffic["1:00-2:00AM"].fillna(0, inplace = True)
df_traffic["2:00-3:00AM"].fillna(0, inplace = True)
df_traffic["3:00-4:00AM"].fillna(0, inplace = True)
df_traffic["4:00-5:00AM"].fillna(0, inplace = True)
df_traffic["5:00-6:00AM"].fillna(0, inplace = True)
df_traffic["6:00-7:00AM"].fillna(0, inplace = True)
df_traffic["7:00-8:00AM"].fillna(0, inplace = True)
df_traffic["8:00-9:00AM"].fillna(0, inplace = True)
df_traffic["9:00-10:00AM"].fillna(0, inplace = True)
df_traffic["10:00-11:00AM"].fillna(0, inplace = True)
df_traffic["11:00-12:00PM"].fillna(0, inplace = True)
df_traffic["12:00-1:00PM"].fillna(0, inplace = True)
df_traffic["1:00-2:00PM"].fillna(0, inplace = True)
df_traffic["2:00-3:00PM"].fillna(0, inplace = True)
df_traffic["3:00-4:00PM"].fillna(0, inplace = True)
df_traffic["4:00-5:00PM"].fillna(0, inplace = True)
df_traffic["5:00-6:00PM"].fillna(0, inplace = True)
df_traffic["6:00-7:00PM"].fillna(0, inplace = True)
df_traffic["7:00-8:00PM"].fillna(0, inplace = True)
df_traffic["8:00-9:00PM"].fillna(0, inplace = True)
df_traffic["9:00-10:00PM"].fillna(0, inplace = True)
df_traffic["10:00-11:00PM"].fillna(0, inplace = True)
df_traffic["11:00-12:00AM"].fillna(0, inplace = True)


#print(df_traffic.head())

#Creando un nuevo dataframe
df_traffic_clean = df_traffic.copy()

#Guardando en un CSV
df_traffic_clean.to_csv('traffic_clean_prueba.csv', sep=',', index=False)