# 📊 Supermarket Sales & Performance Dashboard

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-Visualizations-blueviolet.svg)](https://plotly.com/)
[![Status](https://img.shields.io/badge/Status-Live-success.svg)](https://tu-enlace-de-render.onrender.com)

Tablero analítico e interactivo desarrollado en **Python** para explorar, filtrar y visualizar el rendimiento comercial de una cadena minorista. Diseñado para optimizar la toma de decisiones estratégicas mediante la exploración dinámica de métricas de ventas y comportamiento geográfico.

🔗 **[Ver Aplicación en Vivo](https://supermarket-sales-dashboard-01ij.onrender.com/)**

---

## 🚀 Características Principales

* **Filtros Dinámicos en Tiempo Real:** Segmentación de la información según región geográfica, categoría de producto y segmento de clientes.
* **Panel de KPIs Financieros:** Visualización instantánea de venta total, volumen de pedidos, ticket promedio y base de clientes únicos.
* **Visualizaciones Interactivas (Plotly):**
  * Tendencia temporal de ventas mensuales.
  * Distribución porcentual de ventas por región.
  * Rendimiento comercial por subcategoría de productos.
  * Top 10 de productos más vendidos.
* **Explorador de Datos Detallados:** Vista tabular integrada para auditar y analizar registros específicos filtrados por el usuario.

---

## 🛠️ Tecnologías y Librerías Utilizadas

* **Python:** Lenguaje principal de programación y lógica de datos.
* **Pandas:** Manipulación, limpieza, indexación y agregación del dataset.
* **Streamlit:** Construcción de la interfaz web interactiva y gestión de componentes de usuario.
* **Plotly Express:** Generación de gráficos dinámicos, modernos y responsivos.
* **Render:** Despliegue y alojamiento en la nube (Cloud Hosting).

---

## 📂 Estructura del Proyecto

```text
supermarket-dashboard/
│
├── app.py              # Código principal de la aplicación Streamlit
├── supermarket.csv     # Dataset analizado (registros de ventas minoristas)
├── requirements.txt    # Dependencias del proyecto (Streamlit, Pandas, Plotly)
└── README.md           # Documentación del proyecto

Ejecución Local (Instalación)
Si deseas clonar y ejecutar este proyecto en tu entorno local, sigue estos pasos:

1.- Clona el repositorio:
      git clone [https://github.com/tu-usuario/supermarket-dashboard.git](https://github.com/tu-usuario/supermarket-dashboard.git)
      cd supermarket-dashboard

2.- Instala las dependencias necesarias:
      pip install -r requirements.txt

3.- Ejecuta la aplicación de Streamlit:
      streamlit run app.py
