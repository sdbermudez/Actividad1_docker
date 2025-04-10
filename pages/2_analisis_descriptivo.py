import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("deporte_fisico.csv")

st.title("Análisis Descriptivo")
st.dataframe(df)

# Gráfico: Top 10 departamentos con mayor actividad física
top_10 = df.sort_values("Valor", ascending=False).head(10)
fig = px.bar(top_10, x="Departamento", y="Valor", color="Departamento",
             title="Top 10 departamentos con mayor actividad física")
st.plotly_chart(fig, use_container_width=True)
