import networkx as nx
import pandas as pd


def identify_efficient_monitors(G, top_closeness=20, degree_threshold=100):
    degree = dict(G.degree())
    closeness = nx.closeness_centrality(G)
    
    n = G.number_of_nodes()
    norm_degree = {node: deg / (n - 1) for node, deg in degree.items()}
    
    df = pd.DataFrame({
        'node': list(closeness.keys()),
        'closeness': list(closeness.values()),
        'norm_degree': [norm_degree[n] for n in closeness.keys()],
        'degree': [degree[n] for n in closeness.keys()]
    })
    
    df['close_rank'] = df['closeness'].rank(ascending=False)
    df['deg_rank'] = df['degree'].rank(ascending=False)
    
    efficient = df[
        (df['close_rank'] <= top_closeness) & 
        (df['deg_rank'] > degree_threshold)
    ]
    
    return efficient.sort_values('closeness', ascending=False)


def extract_ego_network(G, node):
    ego = nx.ego_graph(G, node)
    return ego
