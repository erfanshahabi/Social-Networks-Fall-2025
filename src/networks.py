import networkx as nx
import numpy as np


def create_1d_lattice(N, k=2):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    
    for i in range(N):
        for j in range(1, k//2 + 1):
            G.add_edge(i, (i + j) % N)
            G.add_edge(i, (i - j) % N)
    
    return G


def create_2d_lattice(N):
    side = int(np.sqrt(N))
    actual_N = side * side
    
    G = nx.grid_2d_graph(side, side, periodic=True)
    
    mapping = {node: i for i, node in enumerate(G.nodes())}
    G = nx.relabel_nodes(G, mapping)
    
    return G, actual_N


def create_3d_lattice(N):
    side = int(np.cbrt(N))
    actual_N = side ** 3
    
    G = nx.grid_graph(dim=[side, side, side], periodic=False)
    
    mapping = {node: i for i, node in enumerate(G.nodes())}
    G = nx.relabel_nodes(G, mapping)
    
    return G, actual_N


def create_random_network(N, avg_degree=8):
    min_degree = max(8, int(np.log(N)) + 2)
    actual_degree = max(avg_degree, min_degree)
    
    p = actual_degree / (N - 1)
    G = nx.erdos_renyi_graph(N, p)
    
    return G