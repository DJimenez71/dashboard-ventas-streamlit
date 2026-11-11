import streamlit as st
import pandas as pd
import plotly.express as px 

# Configurar página
st.set_page_config(page_title="Dashboard de Ventas", layout="wide")

st.title("📊 Dashboard de Ventas - Superstore")
st.markdown("Análisis interactivo de ventas y ganancias.")

# Cargar datos y convertir fechas
@st.cache_data 
def cargar_datos():
    df = pd.read_csv("data/Superstore_Orders.csv")
    
    # Convertimos a fecha real
    df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
    
    # Creamos columnas de Año y Mes por si las necesitamos luego
    df["Año"] = df["Order Date"].dt.year
    df["Mes"] = df["Order Date"].dt.month_name()

    # Convertir la columna Sales a número
    df["Sales"] = df["Sales"].astype(str).str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
    df["Sales"] = pd.to_numeric(df["Sales"], errors='coerce')
    
    return df

df = cargar_datos()

# FILTRO INTERACTIVO
st.sidebar.header("Filtros")
opciones_regiones = ["Todas"] + list(df["Region"].unique()) #crear lista con regiones

#menú
region_seleccionada = st.sidebar.selectbox("Selecciona una Región", opciones_regiones)

# logica
if region_seleccionada == "Todas":
    df_filtrado = df
else:
    df_filtrado = df[df["Region"] == region_seleccionada]

#mostrar 
st.subheader(f"Datos de la Región: {region_seleccionada}")
st.write(f"Se encontraron {len(df_filtrado)} órdenes.")
st.dataframe(df_filtrado.head(10))  # Mostrar solo las primeras 10 filas

st.markdown("---")
st.subheader("Análisis de Ventas y Ganancias")

# Agrupar los datos
ventas_categoria = df_filtrado.groupby("Category", as_index=False)["Sales"].sum()

# Grafico
fig = px.bar (
    ventas_categoria,
    x="Category",
    y="Sales",
    color="Category",
    title=f"Ventas Totales en la región:{region_seleccionada}",
    labels={"Sales": "Ventas ($)", "Category": "Categoría"}
)

# Formato de eje y
fig.update_yaxes(tickformat="$.2s") 

# mostrar
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("Evolución de Ventas en el tiempo")

#agrupar por año y mes, y sumar ventas
ventas_tiempo = df_filtrado.groupby(["Año", "Mes"], as_index=False)["Sales"].sum()

# Grafico
fig_lineas = px.line(
    ventas_tiempo,
    x="Mes",
    y="Sales",
    color="Año",
    markers=True,
    title=f"Tendencia de Ventas por Mes y Año: {region_seleccionada}",
    labels={"Sales": "Ventas ($)", "Mes": "Mes", "Año": "Año"}
)

# Formato de eje y
fig_lineas.update_yaxes(tickformat="$.2s") 

st.plotly_chart(fig_lineas, use_container_width=True)

# --- FOOTER ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 14px;'>
    Dashboard desarrollado por <b>Daniela Jimenez</b>.<br>
    Datos obtenidos de <a href='https://www.kaggle.com/datasets/yesshivam007/superstore-dataset' target='_blank'>Kaggle (Superstore Dataset)</a>.
    </div>
    """, 
    unsafe_allow_html=True
)