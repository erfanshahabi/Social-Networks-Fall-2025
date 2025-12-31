import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def barabasi_albert_model(N, m):
    if m < 1 or m >= N:
        raise ValueError("m must be between 1 and N-1")
    G = nx.barabasi_albert_graph(N, m)
    return G


def deterministic_scale_free_construction(iterations):
    G = nx.Graph()
    G.add_edges_from([(0, 1), (1, 2), (2, 0)])
    next_node = 3
    
    for iteration in range(iterations):
        edges = list(G.edges())
        edge_scores = []
        
        for u, v in edges:
            score = G.degree(u) + G.degree(v)
            edge_scores.append((score, (u, v)))
        
        edge_scores.sort(reverse=True)
        selected_edge = edge_scores[0][1]
        u, v = selected_edge
        
        new_node = next_node
        next_node += 1
        
        G.remove_edge(u, v)
        G.add_edge(new_node, u)
        G.add_edge(new_node, v)
    
    return G


def analyze_degree_distribution(G):
    degrees = [G.degree(n) for n in G.nodes()]
    degree_counts = {}
    
    for d in degrees:
        degree_counts[d] = degree_counts.get(d, 0) + 1
    
    stats = {
        'min_degree': min(degrees),
        'max_degree': max(degrees),
        'avg_degree': np.mean(degrees),
        'degree_distribution': degree_counts
    }
    
    return stats


def plot_degree_distribution_comparison(G_BA, G_det, save_path='results/plots/degree_distribution.png'):
    import os
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    degrees_BA = [G_BA.degree(n) for n in G_BA.nodes()]
    degree_counts_BA = {}
    for d in degrees_BA:
        degree_counts_BA[d] = degree_counts_BA.get(d, 0) + 1
    
    degrees_sorted_BA = sorted(degree_counts_BA.keys())
    counts_BA = [degree_counts_BA[d] for d in degrees_sorted_BA]
    
    ax1.loglog(degrees_sorted_BA, counts_BA, 'bo-', markersize=8, linewidth=2)
    ax1.set_xlabel('Degree k', fontsize=12)
    ax1.set_ylabel('Count', fontsize=12)
    ax1.set_title('Barabási-Albert Model', fontsize=14)
    ax1.grid(True, alpha=0.3)
    
    degrees_det = [G_det.degree(n) for n in G_det.nodes()]
    degree_counts_det = {}
    for d in degrees_det:
        degree_counts_det[d] = degree_counts_det.get(d, 0) + 1
    
    degrees_sorted_det = sorted(degree_counts_det.keys())
    counts_det = [degree_counts_det[d] for d in degrees_sorted_det]
    
    ax2.loglog(degrees_sorted_det, counts_det, 'ro-', markersize=8, linewidth=2)
    ax2.set_xlabel('Degree k', fontsize=12)
    ax2.set_ylabel('Count', fontsize=12)
    ax2.set_title('Deterministic Scale-Free', fontsize=14)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig


def visualize_networks(G_BA, G_det, save_path='results/plots/network_visualization.png'):
    import os
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    pos_BA = nx.spring_layout(G_BA, k=1, iterations=50)
    degrees_BA = [G_BA.degree(n) for n in G_BA.nodes()]
    node_sizes_BA = [50 + 20 * d for d in degrees_BA]
    
    nx.draw(G_BA, pos_BA, ax=ax1, node_size=node_sizes_BA, 
            node_color='lightblue', edge_color='gray', 
            width=0.5, with_labels=False, alpha=0.8)
    ax1.set_title('Barabási-Albert Model', fontsize=14)
    ax1.axis('off')
    
    pos_det = nx.spring_layout(G_det, k=1, iterations=50)
    degrees_det = [G_det.degree(n) for n in G_det.nodes()]
    node_sizes_det = [50 + 20 * d for d in degrees_det]
    
    nx.draw(G_det, pos_det, ax=ax2, node_size=node_sizes_det, 
            node_color='lightcoral', edge_color='gray', 
            width=0.5, with_labels=False, alpha=0.8)
    ax2.set_title('Deterministic Scale-Free', fontsize=14)
    ax2.axis('off')
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig


def plot_adjacency_matrix(G_BA, G_det, save_path='results/plots/adjacency_matrix.png'):
    import os
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    adj_BA = nx.adjacency_matrix(G_BA).todense()
    im1 = ax1.imshow(adj_BA, cmap='Blues', interpolation='nearest')
    ax1.set_title('BA Model - Adjacency Matrix', fontsize=14)
    ax1.set_xlabel('Node Index')
    ax1.set_ylabel('Node Index')
    plt.colorbar(im1, ax=ax1)
    
    adj_det = nx.adjacency_matrix(G_det).todense()
    im2 = ax2.imshow(adj_det, cmap='Reds', interpolation='nearest')
    ax2.set_title('Deterministic - Adjacency Matrix', fontsize=14)
    ax2.set_xlabel('Node Index')
    ax2.set_ylabel('Node Index')
    plt.colorbar(im2, ax=ax2)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig


def plot_sorted_adjacency_matrix(G_BA, G_det, save_path='results/plots/sorted_adjacency_matrix.png'):
    import os
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    degrees_BA = dict(G_BA.degree())
    nodes_BA_sorted = sorted(degrees_BA.keys(), key=lambda x: degrees_BA[x], reverse=True)
    adj_BA = nx.adjacency_matrix(G_BA, nodelist=nodes_BA_sorted).todense()
    
    im1 = ax1.imshow(adj_BA, cmap='Blues', interpolation='nearest')
    ax1.set_title('BA Model - Sorted by Degree', fontsize=14)
    ax1.set_xlabel('Node Index (sorted)')
    ax1.set_ylabel('Node Index (sorted)')
    plt.colorbar(im1, ax=ax1)
    
    degrees_det = dict(G_det.degree())
    nodes_det_sorted = sorted(degrees_det.keys(), key=lambda x: degrees_det[x], reverse=True)
    adj_det = nx.adjacency_matrix(G_det, nodelist=nodes_det_sorted).todense()
    
    im2 = ax2.imshow(adj_det, cmap='Reds', interpolation='nearest')
    ax2.set_title('Deterministic - Sorted by Degree', fontsize=14)
    ax2.set_xlabel('Node Index (sorted)')
    ax2.set_ylabel('Node Index (sorted)')
    plt.colorbar(im2, ax=ax2)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig


def calculate_blockiness(G):
    adj = nx.adjacency_matrix(G).todense()
    N = adj.shape[0]
    
    block_size = max(1, int(np.sqrt(N)))
    num_blocks = N // block_size
    
    if num_blocks == 0:
        return np.array([[0]])
    
    block_density = np.zeros((num_blocks, num_blocks))
    
    for i in range(num_blocks):
        for j in range(num_blocks):
            block = adj[i*block_size:(i+1)*block_size, j*block_size:(j+1)*block_size]
            block_density[i, j] = np.sum(block) / (block_size * block_size)
    
    return block_density


def compare_blockiness(G_BA, G_det, save_path='results/plots/blockiness_comparison.png'):
    import os
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    block_BA = calculate_blockiness(G_BA)
    im1 = ax1.imshow(block_BA, cmap='Blues', interpolation='nearest')
    ax1.set_title('BA Model - Block Density', fontsize=14)
    ax1.set_xlabel('Block Index')
    ax1.set_ylabel('Block Index')
    plt.colorbar(im1, ax=ax1)
    
    block_det = calculate_blockiness(G_det)
    im2 = ax2.imshow(block_det, cmap='Reds', interpolation='nearest')
    ax2.set_title('Deterministic - Block Density', fontsize=14)
    ax2.set_xlabel('Block Index')
    ax2.set_ylabel('Block Index')
    plt.colorbar(im2, ax=ax2)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig