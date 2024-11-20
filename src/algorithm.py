import random
import networkx as nx
import numpy as np

def gerar_grafo(n, p):
    """
    Gera um grafo aleatório com n vértices e probabilidade p de aresta.
    """
    G = nx.Graph()
    G.add_nodes_from(range(n))  # Adiciona os vértices

    for u in range(n):
        for v in range(u + 1, n):
            if random.random() < p:  # Adiciona a aresta com probabilidade p
                G.add_edge(u, v)
    
    return G

def calcular_propriedades(G):
    """
    Calcula propriedades do grafo: número de arestas, graus, e diâmetro.
    """
    num_vertices = G.number_of_nodes()
    num_arestas = G.number_of_edges()
    graus = [d for _, d in G.degree()]

    grau_min = min(graus) if graus else 0
    grau_max = max(graus) if graus else 0
    grau_medio = np.mean(graus) if graus else 0

    # Calcula o diâmetro apenas se o grafo for conectado
    if nx.is_connected(G) and num_vertices > 1:
        diametro = nx.diameter(G)
    else:
        diametro = 'N/A'  # Representa que o diâmetro não pode ser calculado
    
    return num_vertices, num_arestas, grau_min, grau_max, grau_medio, diametro
