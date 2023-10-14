import streamlit as st
import pandas as pd

df = pd.read_csv('defunciones.csv', sep=';')

st.title('Visualización de los primeros 100 registros')

st.write(df.head(100))

st.title('Filtro de Datos por Año')

selec_ano = st.selectbox('Selecciona un año:', df['ano'].unique())

filtro_dfano = df[df['ano'] == selec_ano]
st.write(filtro_dfano)

st.title('Filtro de Datos por sexo')

selec_sexo = st.selectbox('Selecciona un sexo:', df['sexo_fallecido'].unique())

filtro_dfsexo = df[df['sexo_fallecido'] == selec_sexo]
st.write(filtro_dfsexo)

st.title('Filtrar Datos por Fecha')
df['fecha_defuncion'] = pd.to_datetime(df['fecha_defuncion']).dt.date


inicio = st.date_input('Selecciona una fecha de inicio:', value=df['fecha_defuncion'].min(), min_value=df['fecha_defuncion'].min(), max_value=df['fecha_defuncion'].max())


fin = st.date_input('Selecciona una fecha de fin:', value=df['fecha_defuncion'].max(), min_value=inicio, max_value=df['fecha_defuncion'].max())

fil_fecha = df[(df['fecha_defuncion'] >= inicio) & (df['fecha_defuncion'] <= fin)]

st.write(fil_fecha)

st.title('Filtro de Datos por aseguradora')

selec_ase = st.selectbox('Selecciona una aseguradora:', df['nombre_administradora'].unique())

filtro_dfase = df[df['nombre_administradora'] == selec_ase]
st.write(filtro_dfase)

st.title('Filtro de Datos por mayor de edad')

def mayor_edad(edad_fallecido):
    return edad_fallecido > 18

filtro_mayor = df[mayor_edad(df["edad_fallecido"])]
st.write(filtro_mayor)

st.title('Filtro de Datos por menor de edad')

def menor_edad(edad_fallecido):
    return edad_fallecido < 18

filtro_menor = df[menor_edad(df["edad_fallecido"])]
st.write(filtro_menor)

st.title('Filtro de Datos por tipo de muerte')

selec_mue = st.selectbox('Seleccione tipo de muerte:', df['probable_manera_muerte'].unique())

filtro_mue = df[df['probable_manera_muerte'] == selec_mue]
st.write(filtro_mue)

st.title('Filtro de Datos por municipio')

selec_muni = st.selectbox('Seleccione municipio:', df['municipio_residencia'].unique())

filtro_muni = df[df['municipio_residencia'] == selec_muni]
st.write(filtro_muni)

st.title('Filtro de Datos por localidad')

selec_loca = st.selectbox('Seleccione localida:', df['localidad'].unique())

filtro_loca = df[df['localidad'] == selec_loca]
st.write(filtro_loca)