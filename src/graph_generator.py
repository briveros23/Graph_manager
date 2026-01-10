import pandas as pd
import igraph as ig
from pathlib import Path

class GraphBuilder:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph = ig.Graph(directed=directed)

    def load_csv(self, file):
        """Lee un CSV desde un archivo o buffer"""
        df = pd.read_csv(file)
        required = {"source", "target"}
        if not required.issubset(df.columns):
            raise ValueError("El CSV debe contener 'source' y 'target'")
        return df

    def add_edges_from_df(self, df):
        """Agrega aristas al grafo"""
        edges = list(zip(df["source"], df["target"]))
        self.graph.add_vertices(
            list(set(df["source"]).union(set(df["target"])))
        )
        self.graph.add_edges(edges)

        if "weight" in df.columns:
            self.graph.es["weight"] = df["weight"]

    def build_from_files(self, files):
        """Construye el grafo a partir de múltiples CSV"""
        for file in files:
            df = self.load_csv(file)
            self.add_edges_from_df(df)

        return self.graph

