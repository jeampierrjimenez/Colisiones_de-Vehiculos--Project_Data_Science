import pandas as pd
import numpy as np
import pickle
import plotly.express as px
import streamlit as st

# url = "http://vps-2671696-x.dattaweb.com/traffic/model/"
# response = requests.get(url, timeout=0.5)
# df = pd.DataFrame(response.json()["data"])

df = pd.read_csv(r"C:\Users\franc\OneDrive\Documentos\Henry\proyectos\PROYECTO_GRUPAL\SEMANA 4\calle_barrio_le.csv")

def estado_calles(barrio, hora, df):

    predecir = df[df.Boro_le == barrio]
    predecir['hora'] = hora
    predecir = predecir[['hora', 'Boro_le', 'street_le']].drop_duplicates()

    filename = r"C:\Users\franc\OneDrive\Documentos\Henry\proyectos\PROYECTO_GRUPAL\SEMANA 4\modelo.sav"
    tree = pickle.load(open(filename, 'rb'))

    estado = tree.predict(predecir)
    resultado = pd.DataFrame()
    resultado['street_le'] = predecir.street_le
    resultado['estado'] = estado

    resultado = pd.merge(resultado, df, on = "street_le", how = "inner")
    resultado = resultado[["street", "estado"]]

    resultado = resultado.drop_duplicates()

    return resultado.sort_values("estado", ascending = False)


# res = estado_calles(0, 16, df)

barrio = st.selectbox('barrio', ("Manhattan", "Queens", "Bronx", "Staten Island", "Brooklyn"))

hora = st.selectbox('hora', (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))

if(barrio == "Brooklyn"):
    barrio = 1
elif(barrio == "Staten Island"):
    barrio = 4
elif(barrio == "Queens"):
    barrio = 3
elif(barrio == "Bronx"):
    barrio = 0
elif(barrio == "Manhattan"):
    barrio = 2

st.table(estado_calles(barrio, hora, df).reset_index(drop = True))
