import pandas as pd
import plotly.express as px
import streamlit as st


#configuracion de la pagina

st.set_page_config(
    page_title="Dashboard Supermercado",
    layout="wide",
    page_icon="🛒"
)
#cargar y  preparar datos
@st.cache_data
def load_data():
    df = pd.read_csv('supermarket.csv')
    #convertir fecha para tener el formato correcto
    df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
    return df


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
    "Selecciona la categoria: ", categories, default=categories
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
st.title("Dashboard Analitio de supermercado")
st.markdown(
    "Este tablero interactivo analizael rendimiento de ventas, distribucion por "
    " categorias y comportamiento geografico ."
)
st.markdown("----")

if filtered_df.empty:
    st.warning(
        "No hay datos que coinciden con los filtros seleccionados. Por favor, amplia tu seleccion"
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
        st.metric(label = "Clientes unicos", value = f"{total_customers:,}")    


    st.markdown("---")

    #graficos fila 1

    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        st.subheader("Tendencia de ventasmensiales")
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
                "Sales": "Ventas Totales (S)",
            },
                    )