import matplotlib.pyplot as plt
import networkx as nx
import os
import numpy as np


def plot_degree_eigenvector_scatter(df, save_path='results/plots/gap_analysis.png'):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['degree'], df['eigenvector'], alpha=0.6, s=100, c='blue')
    ax.set_xlabel('Degree', fontsize=12)
    ax.set_ylabel('Eigenvector Centrality', fontsize=12)
    ax.set_title('Degree vs Eigenvector Centrality', fontsize=14)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    return fig


def plot_betweenness_ranking(df, top_n=10, save_path='results/plots/betweenness_ranking.png'):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    top_df = df.nsmallest(top_n, 'bet_rank')
    
    x = range(len(top_df))
    ax.bar(x, top_df['betweenness'], alpha=0.7, color='steelblue')
    ax.set_xticks(x)
    ax.set_xticklabels(top_df['node'], rotation=45, ha='right')
    ax.set_xlabel('Node', fontsize=12)
    ax.set_ylabel('Betweenness Centrality', fontsize=12)
    ax.set_title(f'Top {top_n} Betweenness Centrality', fontsize=14)
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    return fig


def plot_efficiency_scatter(df, save_path='results/plots/efficiency_scatter.png'):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['norm_degree'], df['closeness'], alpha=0.6, s=100, c='green')
    ax.set_xlabel('Normalized Degree', fontsize=12)
    ax.set_ylabel('Closeness Centrality', fontsize=12)
    ax.set_title('Efficiency: Normalized Degree vs Closeness', fontsize=14)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    return fig


def plot_ego_network(G, ego_graph, central_node, save_path='results/plots/ego_network.png'):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    fig, ax = plt.subplots(figsize=(10, 10))
    pos = nx.spring_layout(ego_graph, k=2, iterations=50, seed=42)
    degrees = dict(ego_graph.degree())
    node_sizes = [300 + 50 * degrees[n] for n in ego_graph.nodes()]
    node_colors = ['red' if n == central_node else 'lightblue' for n in ego_graph.nodes()]
    
    nx.draw(ego_graph, pos, ax=ax, 
            node_size=node_sizes,
            node_color=node_colors,
            edge_color='gray',
            width=1,
            with_labels=True,
            font_size=8,
            alpha=0.8)
    
    ax.set_title(f'Ego Network of Node {central_node}', fontsize=14)
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    return fig


def plot_bonacich_trajectories(df, save_path='results/plots/bonacich_trajectories.png'):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    rank_cols = [col for col in df.columns if 'rank_' in str(col)]
    
    import matplotlib.cm as cm
    colors = cm.rainbow(np.linspace(0, 1, len(df)))
    
    for idx, (node_id, row) in enumerate(df.iterrows()):
        ranks = [row[col] for col in rank_cols]
        ax.plot(range(len(rank_cols)), ranks, marker='o', alpha=0.3, color=colors[idx], linewidth=0.5)
    
    ax.set_xticks(range(len(rank_cols)))
    ax.set_xticklabels([col.replace('rank_', 'β=') for col in rank_cols])
    ax.set_xlabel('Power Regime', fontsize=12)
    ax.set_ylabel('Rank', fontsize=12)
    ax.set_title('Bonacich Power: Rank Trajectories', fontsize=14)
    ax.invert_yaxis()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    return fig