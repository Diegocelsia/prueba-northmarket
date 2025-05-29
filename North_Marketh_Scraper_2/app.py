import pandas as pd
import streamlit as st


df = pd.read_excel("seguidores.xlsx", engine='openpyxl')

st.title("Análisis de Seguidores - North Marketh")

filtro_cuenta = st.multiselect("Filtrar por cuenta origen", options=df["Cuenta Origen"].unique(), default=df["Cuenta Origen"].unique())
filtro_contacto = st.slider("Probabilidad de contacto mínima", 0, 3, 1)

df_filtrado = df[(df["Cuenta Origen"].isin(filtro_cuenta)) & (df["Probabilidad contacto"] >= filtro_contacto)]

st.dataframe(df_filtrado)

st.download_button("📥 Descargar Excel", data=df_filtrado.to_csv(index=False).encode(), file_name="seguidores_filtrados.csv", mime="text/csv")
