import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Título
st.markdown("# Departamento")
st.write("Filtrar por % de actividad física:")

# Carga de datos
df = pd.read_csv("deporte_fisico.csv")
geojson_path = "colombia_departamentos.geojson"

# Validación de columna
columna = "Valor"
if columna not in df.columns:
    st.error(f"La columna '{columna}' no está en el DataFrame.")
    st.stop()

# Filtro de porcentaje
filtro = st.slider("Filtrar por % de actividad física:", 0, 100, (30, 70))

df_filtrado = df[(df[columna] >= filtro[0]) & (df[columna] <= filtro[1])]

# Crear el mapa centrado en Colombia
m = folium.Map(location=[4.5709, -74.2973], zoom_start=5)

# Agregar capa coroplética
folium.Choropleth(
    geo_data=geojson_path,
    name="Choropleth",
    data=df_filtrado,
    columns=["Departamento", columna],
    key_on="feature.properties.NOMBRE_DPT",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="% Actividad Física"
).add_to(m)

# Agregar puntos individuales (si se tienen coordenadas)
if "Latitud" in df_filtrado.columns and "Longitud" in df_filtrado.columns:
    for _, row in df_filtrado.iterrows():
        folium.CircleMarker(
            location=[row["Latitud"], row["Longitud"]],
            radius=5,
            popup=row["Departamento"],
            color="blue",
            fill=True,
            fill_color="blue"
        ).add_to(m)

# Mostrar el mapa en Streamlit
st_data = st_folium(m, width=700, height=500)
