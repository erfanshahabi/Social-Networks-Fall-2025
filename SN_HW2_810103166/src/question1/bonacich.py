import networkx as nx
import numpy as np
import pandas as pd


def calculate_bonacich_power(G, beta=0, alpha=1):
    A = nx.adjacency_matrix(G).todense()
    n = A.shape[0]
    I = np.eye(n)
    
    if beta == 0:
        centrality = np.array(np.sum(A, axis=1)).flatten()
    else:
        try:
            inv_matrix = np.linalg.inv(I - beta * A)
            centrality = np.array(alpha * inv_matrix @ np.ones((n, 1))).flatten()
        except np.linalg.LinAlgError:
            centrality = np.array(np.sum(A, axis=1)).flatten()
    
    nodes = list(G.nodes())
    result = {nodes[i]: float(centrality[i]) for i in range(n)}
    
    return result


def analyze_power_regimes(G, beta_values=None):
    if beta_values is None:
        beta_values = [0, 0.01, -0.01]
    
    results = {}
    
    for beta in beta_values:
        power = calculate_bonacich_power(G, beta=beta)
        results[f'power_{beta}'] = power
    
    nodes = list(G.nodes())
    df = pd.DataFrame(index=nodes)
    
    for beta in beta_values:
        power_col = f'power_{beta}'
        df[power_col] = pd.Series(results[power_col])
    
    for beta in beta_values:
        power_col = f'power_{beta}'
        rank_col = f'rank_{beta}'
        df[rank_col] = df[power_col].rank(ascending=False)
    
    return df