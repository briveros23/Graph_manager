from graph_generator import GraphBuilder
import streamlit as st
import igraph as ig
import matplotlib.pyplot as plt

st.title("Construcción de grafo desde múltiples CSV")

uploaded_files = st.file_uploader(
    "Sube uno o varios CSV",
    type=["csv"],
    accept_multiple_files=True
)

if uploaded_files:
    builder = GraphBuilder(directed=True)

    try:
        graph = builder.build_from_files(uploaded_files)

        st.success("Grafo construido correctamente")
        st.write(f"Nodos: {graph.vcount()}")
        st.write(f"Aristas: {graph.ecount()}")

        if st.checkbox("Mostrar nodos"):
            st.write(graph.vs["name"])

        if st.checkbox("Mostrar aristas"):
            st.write(graph.get_edgelist())

        # -------------------------
        # Visualización del grafo
        # -------------------------
        if st.checkbox("Mostrar grafo"):
            fig, ax = plt.subplots(figsize=(5,5))  # tamaño pequeño
            layout = graph.layout("fr")  # Fruchterman-Reingold (popular)
            ig.plot(
                graph,
                target=ax,
                layout=layout,
                vertex_size=20,
                vertex_color="skyblue",
                vertex_label=graph.vs["name"],
                edge_color="gray",
                bbox=(200,200),
                margin=20
            )
            st.pyplot(fig)

    except Exception as e:
        st.error(str(e))
