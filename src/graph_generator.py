import pandas as pd
import igraph as ig
from pathlib import Path

class DocumentLector:
    def __init__(self):
        pass 
    def csv_reader(self, file):
        """Lee un archivo CSV y devuelve un DataFrame"""
        return pd.read_csv(file)
    def excel_reader(self, file):
        """Lee un archivo Excel y devuelve un DataFrame"""
        return pd.read_excel(file)
    def lector (self, file, name=None):
        """Determina el tipo de archivo y llama al lector adecuado"""
        if name.endswith('.csv'):
            return self.csv_reader(file)
        elif name.endswith('.xlsx'):
            return self.excel_reader(file)
        elif name.endswith('.txt'):
            return self.csv_reader(file)
    


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

