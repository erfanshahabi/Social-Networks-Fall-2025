import networkx as nx
import pandas as pd
import random


def load_signed_network(filepath):
    df = pd.read_csv(filepath)
    G = nx.Graph()
    edge_signs = {}
    
    for _, row in df.iterrows():
        u, v = int(row['u']), int(row['v'])
        sign = int(row['sign'])
        G.add_edge(u, v, sign=sign)
        edge_signs[(min(u,v), max(u,v))] = sign
    
    return G, edge_signs


def compute_line_index(edge_signs, node_to_cluster, alpha=0.5):
    P = 0
    N = 0
    
    for (u, v), sign in edge_signs.items():
        cluster_u = node_to_cluster[u]
        cluster_v = node_to_cluster[v]
        
        if cluster_u != cluster_v and sign == 1:
            P += 1
        elif cluster_u == cluster_v and sign == -1:
            N += 1
    
    line_index = alpha * P + (1 - alpha) * N
    return line_index, P, N


def random_clustering(nodes, num_clusters=4):
    node_to_cluster = {}
    nodes_list = list(nodes)
    random.shuffle(nodes_list)
    
    for i, node in enumerate(nodes_list):
        node_to_cluster[node] = i % num_clusters
    
    return node_to_cluster


def optimize_clustering(G, edge_signs, num_clusters=4, iterations=2000):
    nodes = list(G.nodes())
    best_clustering = random_clustering(nodes, num_clusters)
    best_li, _, _ = compute_line_index(edge_signs, best_clustering)
    
    current_clustering = best_clustering.copy()
    
    for iteration in range(iterations):
        node = random.choice(nodes)
        old_cluster = current_clustering[node]
        new_cluster = random.randint(0, num_clusters - 1)
        
        if new_cluster != old_cluster:
            current_clustering[node] = new_cluster
            current_li, _, _ = compute_line_index(edge_signs, current_clustering)
            
            if current_li < best_li:
                best_li = current_li
                best_clustering = current_clustering.copy()
            else:
                current_clustering[node] = old_cluster
    
    return best_clustering, best_li


def run_line_index_analysis(filepath):
    print(f"\nAnalyzing: {filepath.split('/')[-1]}")
    G, edge_signs = load_signed_network(filepath)
    
    print(f"Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")
    
    print("\n--- Random Clustering ---")
    random.seed(42)
    random_clustering_assignment = random_clustering(G.nodes(), num_clusters=4)
    random_li, random_p, random_n = compute_line_index(edge_signs, random_clustering_assignment)
    
    print(f"Line Index: {random_li:.2f}")
    print(f"P (positive between clusters): {random_p}")
    print(f"N (negative within clusters): {random_n}")
    
    print("\n--- Heuristic Clustering ---")
    print("Optimizing...")
    heuristic_clustering, heuristic_li = optimize_clustering(G, edge_signs, num_clusters=4, iterations=2000)
    _, heuristic_p, heuristic_n = compute_line_index(edge_signs, heuristic_clustering)
    
    print(f"Line Index: {heuristic_li:.2f}")
    print(f"P (positive between clusters): {heuristic_p}")
    print(f"N (negative within clusters): {heuristic_n}")
    print(f"Improvement: {random_li - heuristic_li:.2f}")
    
    return random_li, heuristic_li, heuristic_clustering
