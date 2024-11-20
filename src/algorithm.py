import random
import numpy as np
from collections import deque # Fila de vértices para a BFS

def gerar_grafo(n, p):
    """
    Gera um grafo aleatório com n vértices e probabilidade p de aresta.
    """
    # Inicializa o grafo como um dicionário de listas de adjacência
    G = {i: {'adj': []} for i in range(n)}  # Inicializa cada vértice com uma lista de adjacência vazia

    for u in range(n):
        for v in range(u + 1, n):
            if random.random() < p:  # Adiciona a aresta com probabilidade p
                G[u]['adj'].append(v)
                G[v]['adj'].append(u)
    
    return G

def calcular_graus(G):
    """
    Calcula os graus dos vértices do grafo.
    """
    graus = []
    
    for u in G:
        grau = len(G[u]['adj'])
        graus.append(grau)
    
    return graus

def bfs_diametro(G, s):
    """
    Realiza uma busca em largura (BFS) para calcular a maior distância (diâmetro) a partir de um vértice inicial.
    """
    # Inicializa os atributos dos vértices
    for u in G:
        G[u]['color'] = 'WHITE'
        G[u]['d'] = float('inf')
        G[u]['pi'] = None
    
    # Inicializa o vértice de partida
    G[s]['color'] = 'GRAY'
    G[s]['d'] = 0
    G[s]['pi'] = None
    
    # Inicializa a fila com o vértice de partida
    Q = deque([s])
    
    while Q:
        u = Q.popleft()
        for v in G[u]['adj']:
            if G[v]['color'] == 'WHITE':
                G[v]['color'] = 'GRAY'
                G[v]['d'] = G[u]['d'] + 1
                G[v]['pi'] = u
                Q.append(v)
        G[u]['color'] = 'BLACK'
    
    # Calcula a maior distância (diâmetro) a partir do vértice inicial
    max_distancia = -1  # Inicializa a maior distância como -1

    # for sobre todos os vértices no grafo
    for u in G:
        if G[u]['d'] != float('inf'):
            max_distancia = max(max_distancia, G[u]['d'])
    
    # Se a maior distância ainda for -1, significa que o grafo é desconexo
    if max_distancia == -1:
        return None
    else:
        return max_distancia

def calcular_diametro(G):
    """
    Calcula o diâmetro do grafo.
    """
    diametros = []
    for v in G:
        max_distancia = bfs_diametro(G, v)
        if max_distancia is None:
            return 'N/A'  # Grafo desconexo
        diametros.append(max_distancia)
    
    return max(diametros)

def calcular_propriedades(G):
    """
    Calcula propriedades do grafo: número de arestas, graus, e diâmetro.
    """
    num_vertices = len(G)
    num_arestas = sum(len(G[u]['adj']) for u in G) // 2
    graus = calcular_graus(G)

    if graus:
        grau_min = min(graus)
        grau_max = max(graus)
        grau_medio = np.mean(graus)
    else:
        grau_min = 0
        grau_max = 0
        grau_medio = 0

    diametro = calcular_diametro(G)
    
    return num_vertices, num_arestas, grau_min, grau_max, grau_medio, diametro
