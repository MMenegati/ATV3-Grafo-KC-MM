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
    graus = obter_graus(G)

    # Verifica se a lista de graus não está vazia
    if graus:
        grau_min = min(graus)
        grau_max = max(graus)
        grau_medio = np.mean(graus)
    else:
        # Se a lista de graus estiver vazia, define os valores como 0
        grau_min = 0
        grau_max = 0
        grau_medio = 0

    # Calcula o diâmetro apenas se o grafo for conectado
    if nx.is_connected(G) and num_vertices > 1:
        diametro = nx.diameter(G)
    else:
        diametro = 'N/A'  # Representa que o diâmetro não pode ser calculado
    
    return num_vertices, num_arestas, grau_min, grau_max, grau_medio, diametro

def obter_graus(G):
    graus = []
    
    for vertice, grau in G.degree():
        graus.append(grau)
    
    return graus
