import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------------------------------
# CONFIGURACIÓN INICIAL
# -----------------------------------------------------------
st.set_page_config(
    page_title="Tablero de Inteligencia de Negocios",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Tablero de Inteligencia de Negocios")
st.caption("Universidad Panamericana CDMX — Clase de Business Intelligence")

st.title("📊 Tablero Interactivo – Inteligencia de Negocios")
st.caption("Universidad Panamericana · Campus CDMX")

# -----------------------------------------------------------
# CARGA DE DATOS
# -----------------------------------------------------------
@st.cache_data #Python decorator que permite generar caché y ayuda a cargar los datos sólo una vez
def load_data():
     url="https://docs.google.com/spreadsheets/d/1DhE0u54SoDHL-mPo1_BmpcKBJBih7sIN/edit?usp=sharing&ouid=115616101381241002340&rtpof=true&sd=true"
     modified_url=url.replace('/edit?usp=sharing', '/export?format=xlsx')
     all_sheets=pd.read_excel(modified_url, sheet_name=None)   
     return all_sheets['Switchbacks']

df = load_data()

# -----------------------------------------------------------
# PESTAÑAS PRINCIPALES
# -----------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["📈 Documentación General", "🔍 Datos", "📊 Gráficas"])

# -----------------------------------------------------------
#  TAB 1: Documentación General
# -----------------------------------------------------------
with tab1:
    st.subheader("Documentación general del tablero")
    st.markdown("""
    # 📊 Tablero de Inteligencia de Negocios

**Universidad Panamericana CDMX — Clase de Business Intelligence**
<img src="https://posgrados-panamericana.up.edu.mx/hs-fs/hubfs/logo%20posgrados%20con%20espacio.png?width=137&name=logo%20posgrados%20con%20espacio.png" width=150>

Este repositorio contiene el desarrollo y entrega final de un tablero interactivo creado como parte del curso de **Inteligencia de Negocios** de la **Universidad Panamericana, Campus CDMX**.
El objetivo del proyecto es demostrar habilidades de análisis de datos, visualización y generación de insights accionables para la toma de decisiones.

---

## 📁 Contenido del repositorio

```
├── data/                # Sets de datos utilizados (limpios y/o crudos)
├── notebooks/           # Notebooks para exploración y preparación de datos
├── dashboard/           # Archivos del tablero (Power BI, Tableau, o plataforma usada)
├── assets/              # Imágenes usadas en el README o el tablero
└── README.md            # Documentación del proyecto
```

---

## 🎯 Objetivo del proyecto

El propósito del tablero es:

* Analizar datos relevantes del negocio seleccionado.
* Identificar patrones, tendencias y métricas clave.
* Construir visualizaciones que apoyen la toma de decisiones.
* Presentar conclusiones basadas en evidencia.

---

## 📑 Descripción del conjunto de datos

Breve explicación del dataset (ajusta según tu proyecto):

* **Fuente:** (agregar fuente)
* **Número de registros:** (X)
* **Variables principales:**

  * Ejemplo: ventas, regiones, fechas, categorías, clientes, etc.
* **Periodo analizado:** (ej. 2020–2024)

---

## 🛠️ Herramientas utilizadas

* **Power BI / Tableau / Looker Studio** (indica cuál usaste)
* **Python (pandas, numpy, matplotlib, etc.)** para limpieza y análisis preliminar
* **Excel / Google Sheets** (si aplica)
* **Git y GitHub** para control de versiones

---

## 📌 Preguntas de negocio respondidas

Algunas preguntas que el tablero busca resolver (personaliza las tuyas):

* ¿Cuáles son los productos/servicios con mayor rendimiento?
* ¿Cómo se comportan las ventas en distintas regiones?
* ¿Qué factores influyen en los picos o caídas de desempeño?
* ¿Qué recomendaciones pueden derivarse de los patrones observados?

---

## 📊 Vista general del tablero

*(Agrega imágenes aquí si quieres)*

Ejemplo:

![Dashboard Preview](assets/dashboard_preview.png)

---

## 🚀 Cómo visualizar el tablero

### Opción 1: Archivo local

Descargar el archivo desde `/dashboard/` y abrirlo con:

* **Power BI Desktop**
* **Tableau Public/Desktop**

### Opción 2: Enlace en línea

Si tu tablero está publicado, añade aquí:

🔗 **Enlace al tablero:** *(coloca la URL)*

---

## 📈 Proceso de análisis

1. **Exploración inicial del dataset**
2. **Limpieza y preparación de datos**
3. **Modelado y creación de métricas (DAX, cálculos, etc.)**
4. **Construcción de visualizaciones**
5. **Generación de insights y conclusiones**

---

## 📚 Conclusiones

Resume tus hallazgos principales, por ejemplo:

* Se identificó un incremento del X% en ventas durante…
* La región Y presenta el mayor potencial de crecimiento…
* Se recomienda enfocar recursos en…

*(Ajusta según tus resultados reales.)*

---

## 🧑‍💻 Autora

**Arantza Méndez Rodríguez**
Universidad Panamericana CDMX — Business Intelligence

---

## 📜 Licencia

Este proyecto es únicamente con fines educativos.
    """)

# -----------------------------------------------------------
# TAB 2: Comparaciones
# -----------------------------------------------------------
with tab2:
    st.subheader("Dataset del ejercicio")

    st.dataframe(df)

# -----------------------------------------------------------
# TAB 3: Resumen e Insights
# -----------------------------------------------------------
with tab3:
    st.subheader("Visualizaciones")

    st.write("Hola Mundo")
