from graph_generator import GraphBuilder
from graph_generator import DocumentLector
import streamlit as st
import igraph as ig
import matplotlib.pyplot as plt


st.title("Construcción de grafo desde múltiples CSV")
# barra lateral con instrucciones
st.sidebar.header("Instrucciones")
st.sidebar.markdown("""
1. Sube documentos csv, txt o excel que contengan las columnas 'source','target', opcional 'weight'.
(observacion: los archivos txt seran tratados como csv con separador ',')
2. Seleccione las columas adecuadas. 
""")

uploaded_file = st.file_uploader(
    "Sube uno o varios CSV",
    type=["csv","txt","excel"],
    accept_multiple_files=False,
    help="recuerda que para las archivos txt se usará el separador ','"
)
if uploaded_file is not None:
    name = uploaded_file.name if uploaded_file else None

    df = DocumentLector().lector(uploaded_file, name)
    st.write(name)
    if df is None:
        st.error('No se pudo leer el archivo. Asegúrate de que el formato sea correcto.') 
    else:
        st.write("Vista previa de los datos cargados:")
        st.dataframe(df.head())

    