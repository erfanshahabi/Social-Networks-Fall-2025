import networkx as nx
import numpy as np


def calculate_normalized_degree(G):
    degrees = dict(G.degree())
    n = G.number_of_nodes()
    normalized = {node: deg / (n - 1) for node, deg in degrees.items()}
    return normalized


def calculate_eigenvector_centrality(G, max_iter=1000):
    try:
        return nx.eigenvector_centrality(G, max_iter=max_iter)
    except:
        return nx.eigenvector_centrality_numpy(G)


def calculate_closeness_centrality(G):
    if not nx.is_connected(G):
        return nx.closeness_centrality(G)
    return nx.closeness_centrality(G)


def calculate_all_centralities(G):
    results = {
        'degree': calculate_normalized_degree(G),
        'eigenvector': calculate_eigenvector_centrality(G),
        'closeness': calculate_closeness_centrality(G)
    }
    
    return results
