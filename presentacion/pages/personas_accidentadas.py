import streamlit as st
import requests
import json
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

##llamando api#1
url_injury = "http://vps-2671696-x.dattaweb.com/collision/state_person/"
response_injury = requests.get(url_injury)
injury = pd.DataFrame(response_injury.json()["data"])
injury.columns = injury.columns.str.upper()
injury['TIME_PERIOD']=pd.to_datetime(injury.PERIODO)
injury['YEAR'] = injury['TIME_PERIOD'].dt.strftime('%Y')
injury['MONTH'] = injury['TIME_PERIOD'].dt.strftime('%m')

##llamando api#2
url_sex = "http://vps-2671696-x.dattaweb.com/collision/genere/"
response_sex = requests.get(url_sex)
sex = pd.DataFrame(response_sex.json()["data"])
sex.columns = sex.columns.str.upper()
sex['TIME_PERIOD']=pd.to_datetime(sex.PERIODO)
sex['YEAR'] = sex['TIME_PERIOD'].dt.strftime('%Y')
sex['MONTH'] = sex['TIME_PERIOD'].dt.strftime('%m')

##llamando api#3
url_type = "http://vps-2671696-x.dattaweb.com/collision/type/"
response_type = requests.get(url_type)
type = pd.DataFrame(response_type.json()["data"])
type.columns = type.columns.str.upper()
type['TIME_PERIOD']=pd.to_datetime(type.PERIODO)
type['YEAR'] = type['TIME_PERIOD'].dt.strftime('%Y')
type['MONTH'] = type['TIME_PERIOD'].dt.strftime('%m')

##llamando api#4
url_status = "http://vps-2671696-x.dattaweb.com/collision/status/"
response_status = requests.get(url_status)
status = pd.DataFrame(response_status.json()["data"])
status.columns = status.columns.str.upper()
status['TIME_PERIOD']=pd.to_datetime(status.PERIODO)
status['YEAR'] = status['TIME_PERIOD'].dt.strftime('%Y')
status['MONTH'] = status['TIME_PERIOD'].dt.strftime('%m')

page = st.sidebar.selectbox(
    'Selecciona Análisis', [
        'Visión General',
        'Condición del accidentado',
        'Sexo del accidentado',
        'Rol del accidentado',
        'Estado emocional del accidentado'
        ]
    )

if page == 'Visión General':

    st.markdown("<h1 style='text-align: center;'>Visión General</h1>", unsafe_allow_html=True)

    injury = injury[['PERIODO','YEAR', 'MONTH', 'QTY_INJURED', 'QTY_KILLED', 'QTY_UNSPECIFIED', 'QTY_TOTAL']]
    type = type[['PERIODO','YEAR', 'MONTH','QTY_BICYCLIST', 'QTY_OCCUPANT','QTY_OTHER_MOTORIZED', 'QTY_PEDESTRIAN','QTY_TOTAL']]
    tab1, tab2, tab3 = st.tabs(['Total de Accidentados','Estado del accidentado', 'Tipo de rol'])

    with tab1:

        def plot_total_general(injury):

            st.markdown("<h2 style='text-align: center;'>I. Cantidad Total de Accidentados AÑO-MES (2012-2022)</h2>", unsafe_allow_html=True)

            tracetotal = px.line(
                injury,
                x="PERIODO",
                y="QTY_TOTAL",
                title ='Cantidad de Accidentados 2012 - 2022'
            )
            
            tracetotal.update_xaxes(showgrid=False)
            tracetotal.update_yaxes(showgrid=False)

            st.plotly_chart(tracetotal)

        plot_total_general(injury)

    with tab2:

        def plot_lesionados_general(injury):
        
            st.markdown("<h2 style='text-align: center;'>1.A Cantidad de Accidentados Lesionados AÑO-MES (2012-2022)</h2>", unsafe_allow_html=True)
             
            trace1 = px.line(
                injury,
                x="PERIODO",
                y="QTY_INJURED",
                title ='Cantidad de Accidentados Lesionados 2012 - 2022'
            )

            st.plotly_chart(trace1)

        plot_lesionados_general(injury)

        def plot_fallecidos_general(injury):

            st.markdown("<h2 style='text-align: center;'>1.B Cantidad de Accidentados Fallecidos AÑO-MES (2012-2022)</h2>", unsafe_allow_html=True)

            trace2 = px.line(
                injury,
                x="PERIODO",
                y="QTY_KILLED",
                title ='Cantidad de Accidentados Fallecidos 2012 - 2022'
            )
        
            st.plotly_chart(trace2)
    
        plot_fallecidos_general(injury)

    with tab3:
        
        def plot_ciclistas_general(type):
            
            st.markdown("<h2 style='text-align: center;'>2.A Cantidad de Accidentados Ciclistas AÑO-MES (2012-2022)</h2>", unsafe_allow_html=True)
            
            trace3 = px.line(
                type,
                x="PERIODO",
                y="QTY_BICYCLIST",
                title ='Cantidad de Accidentados Ciclistas 2012 - 2022'
            )
        
            st.plotly_chart(trace3)
    
        plot_ciclistas_general(type)

        def plot_peatones_general(type):
            
            st.markdown("<h2 style='text-align: center;'>2.B Cantidad de Accidentados Peatones AÑO-MES (2012-2022)</h2>", unsafe_allow_html=True)

            trace4 = px.line(
                type,
                x="PERIODO",
                y="QTY_PEDESTRIAN",
                title ='Cantidad de Accidentados Peatones 2012 - 2022'
            )
        
            st.plotly_chart(trace4)

        plot_peatones_general(type)

elif page == 'Condición del accidentado':

    st.markdown("<h1 style='text-align: center;'>Condición del Accidentado</h1>", unsafe_allow_html=True)

    injury = injury[['PERIODO','YEAR', 'MONTH', 'QTY_INJURED', 'QTY_KILLED', 'QTY_UNSPECIFIED', 'QTY_TOTAL']]
    year = injury['YEAR'].unique()

    choose_year_injury = st.selectbox("Escoger año", year)

    tab1, tab2, tab3 = st.tabs(['Lesionados', "Fallecidos", "Sin Especificar"])

    with tab1:
        
        def plot_lesionados_mensual(choose_year_injury, injury):
            
            year_injury = injury['YEAR'] == choose_year_injury
            data_by_year_injury = pd.DataFrame(injury[year_injury])
            
            mes_injury = data_by_year_injury['MONTH']
            injured = data_by_year_injury['QTY_INJURED']
            
            fig1 = px.line(data_by_year_injury, x=mes_injury, y=injured)
            fig1.layout.title = f'Cantidad de Accidentados Lesionados - {choose_year_injury}'
            st.plotly_chart(fig1)

        plot_lesionados_mensual(choose_year_injury, injury)
    
    with tab2:
        
        def plot_fallecidos_mensual(choose_year_injury, injury):
            
            year_injury = injury['YEAR'] == choose_year_injury
            data_by_year_injury = pd.DataFrame(injury[year_injury])
            
            mes_injury = data_by_year_injury['MONTH']
            killed = data_by_year_injury['QTY_KILLED']
            
            fig2 = px.line(data_by_year_injury, x=mes_injury, y=killed)
            fig2.layout.title = f'Cantidad de Accidentados Fallecidos - {choose_year_injury}'
            st.plotly_chart(fig2)

        plot_fallecidos_mensual(choose_year_injury, injury)

    with tab3:

        def plot_sinesp_mensual(choose_year_injury, injury):
            
            year_injury = injury['YEAR'] == choose_year_injury
            data_by_year_injury = pd.DataFrame(injury[year_injury])
            
            mes_injury = data_by_year_injury['MONTH']
            unspecified = data_by_year_injury['QTY_UNSPECIFIED']
            
            fig3 = px.line(data_by_year_injury, x=mes_injury, y=unspecified)
            fig3.layout.title = f'Cantidad de Accidentados Sin Especificar - {choose_year_injury}'
            st.plotly_chart(fig3)
    
        plot_sinesp_mensual(choose_year_injury, injury)

elif page == 'Sexo del accidentado':

    st.markdown("<h1 style='text-align: center;'>Accidentados por Género</h1>", unsafe_allow_html=True)

    sex = sex[['PERIODO','YEAR', 'MONTH', 'QTY_MALE', 'QTY_FEMALE', 'QTY_UNDEFINED', 'QTY_TOTAL']]
    year = sex['YEAR'].unique()
    
    choose_year_sex = st.selectbox("Escoger año", year)

    tab1, tab2, tab3 = st.tabs(['Hombres', "Mujeres", "No especifica"])

    with tab1:

        def plot_hombres_mensual(choose_year_sex, sex):
            
            year_sex = sex['YEAR'] == choose_year_sex
            data_by_year_sex = pd.DataFrame(sex[year_sex])
            
            mes_sex = data_by_year_sex['MONTH']
            male = data_by_year_sex['QTY_MALE']
            
            fig4 = px.line(data_by_year_sex, x=mes_sex, y=male)
            fig4.layout.title = f'Cantidad de Accidentados Hombres - {choose_year_sex}'
            st.plotly_chart(fig4)

        plot_hombres_mensual(choose_year_sex, sex)

    with tab2:

        def plot_mujeres_mensual(choose_year_sex, sex):
            
            year_sex = sex['YEAR'] == choose_year_sex
            data_by_year_sex = pd.DataFrame(sex[year_sex])
            
            mes_sex = data_by_year_sex['MONTH']
            female = data_by_year_sex['QTY_FEMALE']
            
            fig5 = px.line(data_by_year_sex, x=mes_sex, y=female)
            fig5.layout.title = f'Cantidad de Accidentados Mujeres - {choose_year_sex}'
            st.plotly_chart(fig5)

        plot_mujeres_mensual(choose_year_sex, sex)

    with tab3:

        def plot_nodef_mensual(choose_year_sex, sex):
            
            year_sex = sex['YEAR'] == choose_year_sex
            data_by_year_sex = pd.DataFrame(sex[year_sex])

            mes_sex = data_by_year_sex['MONTH']
            undefined = data_by_year_sex['QTY_UNDEFINED']

            fig6 = px.line(data_by_year_sex, x=mes_sex, y=undefined)
            fig6.layout.title = f'Cantidad de Accidentados Sexo No Especifica - {choose_year_sex}'
            st.plotly_chart(fig6)

        plot_nodef_mensual(choose_year_sex, sex)

elif page == 'Rol del accidentado':

    st.markdown("<h1 style='text-align: center;'>Rol del Accidentado</h1>", unsafe_allow_html=True)

    type = type[['PERIODO','YEAR', 'MONTH', 'QTY_BICYCLIST', 'QTY_OCCUPANT', 'QTY_OTHER_MOTORIZED', 'QTY_PEDESTRIAN', 'QTY_TOTAL']]
    year = type['YEAR'].unique()
    
    choose_year_type = st.selectbox("Escoger año", year)

    tab1, tab2, tab3, tab4 = st.tabs(['Ciclistas', "Peatones", "Ocupantes", "Otros Motorizados"])

    with tab1:
        def plot_ciclista_mensual(choose_year_type, type):
            
            year_type = type['YEAR'] == choose_year_type
            data_by_year_type = pd.DataFrame(type[year_type])
            
            mes_type = data_by_year_type['MONTH']
            bicyclist = data_by_year_type['QTY_BICYCLIST']
            
            fig7 = px.line(data_by_year_type, x=mes_type, y=bicyclist)
            fig7.layout.title = f'Cantidad de Accidentados Ciclistas - {choose_year_type}'
            st.plotly_chart(fig7)

        plot_ciclista_mensual(choose_year_type, type)

    with tab2:

        def plot_peaton_mensual(choose_year_type, type):
            
            year_type = type['YEAR'] == choose_year_type
            data_by_year_type = pd.DataFrame(type[year_type])
            
            mes_type = data_by_year_type['MONTH']
            pedestrian = data_by_year_type['QTY_PEDESTRIAN']
            
            fig8 = px.line(data_by_year_type, x=mes_type, y=pedestrian)
            fig8.layout.title = f'Cantidad de Accidentados Peatones - {choose_year_type}'
            st.plotly_chart(fig8)

        plot_peaton_mensual(choose_year_type, type)

    with tab3:

        def plot_ocupante_mensual(choose_year_type, type):
            
            year_type = type['YEAR'] == choose_year_type
            data_by_year_type = pd.DataFrame(type[year_type])
            
            mes_type = data_by_year_type['MONTH']
            occupant = data_by_year_type['QTY_OCCUPANT']
            
            fig9 = px.line(data_by_year_type, x=mes_type, y=occupant)
            fig9.layout.title = f'Cantidad de Accidentados Ocupantes - {choose_year_type}'
            st.plotly_chart(fig9)

        plot_ocupante_mensual(choose_year_type, type)

    with tab4:

        def plot_otro_mensual(choose_year_type, type):
            
            year_type = type['YEAR'] == choose_year_type
            data_by_year_type = pd.DataFrame(type[year_type])
            
            mes_type = data_by_year_type['MONTH']
            other_motorized = data_by_year_type['QTY_OTHER_MOTORIZED']
            
            fig10 = px.line(data_by_year_type, x=mes_type, y=other_motorized)
            fig10.layout.title = f'Cantidad de Accidentados Otros Motorizados - {choose_year_type}'
            st.plotly_chart(fig10)

        plot_otro_mensual(choose_year_type, type)

else:

    st.markdown("<h1 style='text-align: center;'>Estado del Accidentado</h1>", unsafe_allow_html=True)

    status = status[['PERIODO','YEAR', 'MONTH', 'QTY_APPARENT_DEATH', 'QTY_CONSCIOUS', 'QTY_DOES_NOT_APPLY',
                'QTY_INCOHERENT', 'QTY_SEMICONSCIOUS', 'QTY_SHOCK', 'QTY_UNCONSCIOUS', 'QTY_UNKNOWN', 'QTY_TOTAL']]

    year = status['YEAR'].unique()
    choose_year_status = st.selectbox("Escoger año", year)

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(
                                                        ['Muerte Aparente',
                                                        "Consciente",
                                                        "N/A",
                                                        "Incoherente",
                                                        'Semi-consciente',
                                                        "Shock",
                                                        "Inconsciente",
                                                        "Desconocido"]
                                                    )

    with tab1:

        def plot_muer_apa_mensual(choose_year_status, status):
        
            year_status = status['YEAR'] == choose_year_status
            data_by_year_status = pd.DataFrame(status[year_status])
            
            mes_status = data_by_year_status['MONTH']
            apparent_death = data_by_year_status['QTY_APPARENT_DEATH']
            
            fig11 = px.line(data_by_year_status, x=mes_status, y=apparent_death)
            fig11.layout.title = f'Cantidad de Accidentados en Estado de Muerte Aparente - {choose_year_status}'
            st.plotly_chart(fig11)

        plot_muer_apa_mensual(choose_year_status, status)

    with tab2:

        def plot_consciencia_mensual(choose_year_status, status):
        
            year_status = status['YEAR'] == choose_year_status
            data_by_year_status = pd.DataFrame(status[year_status])
            
            mes_status = data_by_year_status['MONTH']
            conscious = data_by_year_status['QTY_CONSCIOUS']
            
            fig12 = px.line(data_by_year_status, x=mes_status, y=conscious)
            fig12.layout.title = f'Cantidad de Accidentados en estado de Consciencia - {choose_year_status}'
            st.plotly_chart(fig12)

        plot_consciencia_mensual(choose_year_status, status)

    with tab3:

        def plot_not_apply_mensual(choose_year_status, status):
        
            year_status = status['YEAR'] == choose_year_status
            data_by_year_status = pd.DataFrame(status[year_status])
            
            mes_status = data_by_year_status['MONTH']
            does_not_apply = data_by_year_status['QTY_DOES_NOT_APPLY']
            
            fig13 = px.line(data_by_year_status, x=mes_status, y=does_not_apply)
            fig13.layout.title = f'Cantidad de Accidentados en estado N/A - {choose_year_status}'
            st.plotly_chart(fig13)

        plot_not_apply_mensual(choose_year_status, status)

    with tab4:

        def plot_incoherencia_mensual(choose_year_status, status):
        
            year_status = status['YEAR'] == choose_year_status
            data_by_year_status = pd.DataFrame(status[year_status])
            
            mes_status = data_by_year_status['MONTH']
            incoherent = data_by_year_status['QTY_INCOHERENT']
            
            fig14 = px.line(data_by_year_status, x=mes_status, y=incoherent)
            fig14.layout.title = f'Cantidad de Accidentados en estado de Incoherencia - {choose_year_status}'
            st.plotly_chart(fig14)

        plot_incoherencia_mensual(choose_year_status, status)

    with tab5:

        def plot_semiconsciencia_mensual(choose_year_status, status):
        
            year_status = status['YEAR'] == choose_year_status
            data_by_year_status = pd.DataFrame(status[year_status])
            
            mes_status = data_by_year_status['MONTH']
            semiconscious = data_by_year_status['QTY_SEMICONSCIOUS']
            
            fig15 = px.line(data_by_year_status, x=mes_status, y=semiconscious)
            fig15.layout.title = f'Cantidad de Accidentados en estado de Semi-consciencia - {choose_year_status}'
            st.plotly_chart(fig15)

        plot_semiconsciencia_mensual(choose_year_status, status)

    with tab6:

        def plot_shock_mensual(choose_year_status, status):

            year_status = status['YEAR'] == choose_year_status
            data_by_year_status = pd.DataFrame(status[year_status])
            
            mes_status = data_by_year_status['MONTH']
            shock = data_by_year_status['QTY_SHOCK']
            
            fig16 = px.line(data_by_year_status, x=mes_status, y=shock)
            fig16.layout.title = f'Cantidad de Accidentados en estado de Shock - {choose_year_status}'
            st.plotly_chart(fig16)

        plot_shock_mensual(choose_year_status, status)

    with tab7:

        def plot_inconsciencia_mensual(choose_year_status, status):
        
            year_status = status['YEAR'] == choose_year_status
            data_by_year_status = pd.DataFrame(status[year_status])
            
            mes_status = data_by_year_status['MONTH']
            unconscious = data_by_year_status['QTY_UNCONSCIOUS']
            
            fig17 = px.line(data_by_year_status, x=mes_status, y=unconscious)
            fig17.layout.title = f'Cantidad de Accidentados en estado de Inconsciencia - {choose_year_status}'
            st.plotly_chart(fig17)

        plot_inconsciencia_mensual(choose_year_status, status)

    with tab8:

        def plot_desconocido_mensual(choose_year_status, status):
        
            year_status = status['YEAR'] == choose_year_status
            data_by_year_status = pd.DataFrame(status[year_status])
            
            mes_status = data_by_year_status['MONTH']
            unknown = data_by_year_status['QTY_UNKNOWN']
            
            fig18 = px.line(data_by_year_status, x=mes_status, y=unknown)
            fig18.layout.title = f'Cantidad de Accidentados en estado Desconocido - {choose_year_status}'
            st.plotly_chart(fig18)

        plot_desconocido_mensual(choose_year_status, status)
    

    



    




