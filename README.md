# 📊 Dashboard de Ventas - Superstore

Este proyecto es un Dashboard interactivo desarrollado en Python que analiza el rendimiento de ventas, categorías de productos y tendencias temporales del dataset global "Superstore". El objetivo es ofrecer una herramienta visual que permita a los tomadores de decisiones filtrar información por región y detectar oportunidades de negocio.

## 🛠️ Herramientas utilizadas
*   **Python** (Pandas para manipulación y limpieza de datos)
*   **Streamlit** (para la creación de la interfaz web interactiva)
*   **Plotly Express** (para gráficos dinámicos e interactivos)
*   **VS Code** y **Git** (control de versiones)

## ⚙️ Características del Dashboard
*   **Filtro dinámico:** Permite seleccionar entre las diferentes regiones (South, West, Central, East) o ver el consolidado global ("Todas").
*   **Vista de datos:** Tabla con las primeras órdenes de la región seleccionada.
*   **Análisis de Categorías:** Gráfico de barras que muestra qué categoría genera más ingresos.
*   **Evolución Temporal:** Gráfico de líneas que muestra la estacionalidad de las ventas mes a mes.

## 📈 Hallazgos Principales (Insights)
Tras filtrar y analizar los datos, se destacan los siguientes resultados:

*   **Global:** La categoría de **Tecnología** es la que genera más ingresos a nivel general. El pico máximo de ventas globales ocurrió en **noviembre de 2017**.
*   **Región South (Sur):** La **Tecnología** domina las ventas. El pico de ingresos más alto se registró en **marzo de 2014**.
*   **Región West (Oeste):** Existe una competencia muy reñida; **Furniture (Muebles)** y **Tecnología** empatan en ingresos. Las ventas se mantuvieron parejas durante el año, pero el pico máximo fue en **diciembre de 2016**.
*   **Región Central:** El rendimiento es muy equilibrado entre categorías, aunque al final del periodo **Office Supplies (Artículos de oficina)** y **Tecnología** toman la delantera. El mejor mes fue **septiembre de 2014**.
*   **Región East (Este):** La **Tecnología** es la categoría líder indiscutible, con un pico de ventas muy marcado en **noviembre de 2017**.

## 🚀 Cómo ejecutar este proyecto localmente
1. Clona este repositorio:
   `git clone https://github.com/DJimenez71/dashboard-ventas-streamlit.git`
2. Instala las dependencias necesarias:
   `pip install streamlit pandas plotly openpyxl`
3. Ejecuta la aplicación:
   `streamlit run streamlit_app.py`

## 📂 Fuentes y Datos
Los datos utilizados en este proyecto provienen del dataset [Superstore Dataset](https://www.kaggle.com/datasets/yesshivam007/superstore-dataset) disponible en Kaggle.

---
*Análisis realizado por Daniela Jimenez como parte de su portafolio de análisis de datos.*
*11 de Noviembre 2026*