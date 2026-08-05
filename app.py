import pandas as pd
import plotly.express as px
import streamlit as st
import os


#configuracion de la pagina

st.set_page_config(
    page_title="Dashboard Supermercado",
    layout="wide",
    page_icon="🛒"
)

# Obtener la ruta absoluta de la carpeta donde está este script (app.py)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(CURRENT_DIR, "supermarket.csv")

#cargar y  preparar datos
@st.cache_data
def load_data():
    df = pd.read_csv(CSV_PATH)
    #convertir fecha para tener el formato correcto
    df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
    return df

df = load_data()
#barra lateral de filtros

st.sidebar.header("Filtros")

#filtro region
regions = df["Region"].unique().tolist()
selected_regions = st.sidebar.multiselect(
    "Selecciona la region: ", regions, default=regions
)

#filtro categoroa

categories = df["Category"].unique().tolist()
selected_categories = st.sidebar.multiselect(
    "Selecciona la categoría: ", categories, default=categories
)

#filtro segmento

segments = df["Segment"].unique().tolist()
selected_segments = st.sidebar.multiselect(
    "Selecciona el segmento: ", segments, default=segments
)

#filtro de dataframe segun la seleccion de usuario
filtered_df =df[
    df["Region"].isin(selected_regions)
    & df["Category"].isin(selected_categories)
    & df["Segment"].isin(selected_segments)
]

#cuerpo principal del dashboard
st.title("Dashboard Analítico de Supermercado")
st.markdown(
    "Este tablero interactivo analiza el rendimiento de ventas, distribución por "
    "categorías y comportamiento geográfico."
)
st.markdown("----")

if filtered_df.empty:
    st.warning(
        "No hay datos que coincidan con los filtros seleccionados. Por favor, amplía tu selección."
    )
else:
    #tarjetas KPi
    total_sales = filtered_df["Sales"].sum()
    total_orders = filtered_df["Order ID"].nunique()
    avg_order_value = total_sales/ total_orders if total_orders > 0 else 0
    total_customers = filtered_df["Customer ID"].nunique()

    col1, col2, col3, col4 = st.columns(4) 

    with col1:
        st.metric(label = "Venta Total", value = f"${total_sales:,.2f}")

    with col2:
        st.metric(label = "Total pedidos", value = f"{total_orders :,}")    

    with col3:
        st.metric(label = "Ticket promedio", value = f"${avg_order_value:,.2f}")   #.2f es para que se vean los decimales

    with col4:
        st.metric(label = "Clientes únicos", value = f"{total_customers:,}")    


    st.markdown("---")

    #graficos fila 1

    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        st.subheader("Tendencia de ventas mensuales")
        #agrupamos por ventas por mes

        monthly_sales = (
            filtered_df.set_index("Order Date")
            .resample("M")["Sales"]
            .sum()
            .reset_index()
        )
        fig_time = px.line(
            monthly_sales,
            x="Order Date",
            y="Sales",
            markers=True,
            labels={
                "Order Date": "Fecha del Periodo",
                "Sales": "Ventas Totales ($)",
            },
            template="plotly_white",
        )
        fig_time.update_traces(line=dict(color="#1F77B4", width=3))
        st.plotly_chart(fig_time, use_container_width=True)

    with col_chart2:
        st.subheader("Ventas por Región")
        region_sales = (
            filtered_df.groupby("Region")["Sales"].sum().reset_index()
        )
        fig_region = px.pie(
            region_sales,
            names="Region",
            values="Sales",
            hole=0.4,
            template="plotly_white",
        )
        st.plotly_chart(fig_region, use_container_width=True)

    #graficos fila 2

    col_chart3, col_chart4 = st.columns(2)
    with col_chart3:
        st.subheader("Ventas por Subcategoría")
        subcat_sales = (
            filtered_df.groupby("Sub-Category")["Sales"]
            .sum()
            .reset_index()
            .sort_values(by="Sales", ascending=True)
        )
        fig_subcat = px.bar(
            subcat_sales,
            x="Sales",
            y="Sub-Category",
            orientation="h",
            labels={
                "Sales": "Ventas Totales ($)",
                "Sub-Category": "Subcategoría",
            },
            template="plotly_white",
        )
        st.plotly_chart(fig_subcat, use_container_width=True)

    with col_chart4:
        st.subheader("Los 10 productos más vendidos")
        top_products = (
            filtered_df.groupby("Product Name")["Sales"]
            .sum()
            .reset_index()
            .sort_values(by="Sales", ascending=False)
            .head(10)
            .sort_values(by="Sales", ascending=True)
        )
        fig_prod = px.bar(
            top_products,
            x="Sales",
            y="Product Name",
            orientation="h",
            labels={"Sales": "Ventas Totales ($)", "Product Name": "Producto"},
            template="plotly_white",
        )
        st.plotly_chart(fig_prod, use_container_width=True)

    #Tabla de datos detallados

    with st.expander(" Ver datos detallados filtrados"):
        st.dataframe(filtered_df, use_container_width=True)