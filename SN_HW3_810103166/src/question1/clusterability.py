import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


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


def detect_clusters_weakly_balanced(G, edge_signs):
    G_pos = nx.Graph()
    G_pos.add_nodes_from(G.nodes())
    
    for (u, v), sign in edge_signs.items():
        if sign == 1:
            G_pos.add_edge(u, v)
    
    clusters = list(nx.connected_components(G_pos))
    
    node_to_cluster = {}
    for i, cluster in enumerate(clusters):
        for node in cluster:
            node_to_cluster[node] = i
    
    return clusters, node_to_cluster


def visualize_clusters(G, edge_signs, node_to_cluster, filename, save_path=None):
    pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
    
    plt.figure(figsize=(12, 8))
    
    num_clusters = max(node_to_cluster.values()) + 1
    colors = plt.cm.Set3(range(num_clusters))
    
    for cluster_id in range(num_clusters):
        nodes = [n for n, c in node_to_cluster.items() if c == cluster_id]
        nx.draw_networkx_nodes(G, pos, nodelist=nodes, 
                              node_color=[colors[cluster_id]], 
                              node_size=300, label=f'Cluster {cluster_id}')
    
    pos_edges = [(u,v) for (u,v), s in edge_signs.items() if s == 1]
    neg_edges = [(u,v) for (u,v), s in edge_signs.items() if s == -1]
    
    nx.draw_networkx_edges(G, pos, edgelist=pos_edges, edge_color='green', width=2)
    nx.draw_networkx_edges(G, pos, edgelist=neg_edges, edge_color='red', 
                          width=1, style='dashed')
    
    nx.draw_networkx_labels(G, pos, font_size=8)
    
    plt.legend()
    plt.title(f'Weakly Balanced Network - {filename}')
    plt.axis('off')
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.tight_layout()
    plt.show()


def detect_clusters(filepath, visualize=True):
    filename = filepath.split('/')[-1]
    print(f"\nAnalyzing: {filename}")
    
    G, edge_signs = load_signed_network(filepath)
    
    clusters, node_to_cluster = detect_clusters_weakly_balanced(G, edge_signs)
    
    print(f"Total clusters: {len(clusters)}")
    for i, cluster in enumerate(clusters):
        nodes = sorted(list(cluster))
        if len(nodes) > 10:
            print(f"  Cluster {i}: {len(nodes)} nodes - {nodes[:10]} ...")
        else:
            print(f"  Cluster {i}: {len(nodes)} nodes - {nodes}")
    
    print("\nMethod: Connected components on positive edges")
    print("Weakly balanced: positive edges within clusters, negative between clusters")
    
    if visualize:
        visualize_clusters(G, edge_signs, node_to_cluster, filename)
    
    return clusters, node_to_cluster
