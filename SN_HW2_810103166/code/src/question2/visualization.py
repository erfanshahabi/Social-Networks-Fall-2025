import matplotlib.pyplot as plt
import numpy as np
import os


def plot_ranking_comparison_scatter(comparison_df, save_path='results/plots/ranking_comparison.png'):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    fig, ax = plt.subplots(figsize=(10, 10))
    
    ax.scatter(comparison_df['pagerank_rank'], comparison_df['authority_rank'], 
               alpha=0.5, s=20, c='blue')
    
    max_rank = max(comparison_df['pagerank_rank'].max(), comparison_df['authority_rank'].max())
    ax.plot([1, max_rank], [1, max_rank], 'r--', alpha=0.5, label='y=x (perfect agreement)')
    
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('PageRank Rank', fontsize=12)
    ax.set_ylabel('HITS Authority Rank', fontsize=12)
    ax.set_title('Ranking Comparison: HITS vs PageRank', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig


def plot_rank_trajectories(trajectories_df, save_path='results/plots/rank_trajectories.png'):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    rank_cols = [col for col in trajectories_df.columns if 'rank_' in col]
    alpha_values = [float(col.split('_')[1]) for col in rank_cols]
    
    for idx, row in trajectories_df.iterrows():
        ranks = [row[col] for col in rank_cols]
        ax.plot(alpha_values, ranks, marker='o', label=f"Node {row['node']}")
    
    ax.set_xlabel('Damping Factor (α)', fontsize=12)
    ax.set_ylabel('Rank', fontsize=12)
    ax.set_title('PageRank Stability: Rank Trajectories', fontsize=14)
    ax.invert_yaxis()
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig


def plot_sensitivity_heatmap(sensitivity_df, top_n=20, save_path='results/plots/sensitivity_heatmap.png'):
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    rank_cols = [col for col in sensitivity_df.columns if 'rank_' in col]
    
    avg_ranks = sensitivity_df[rank_cols].mean(axis=1)
    top_indices = avg_ranks.nsmallest(top_n).index
    top_data = sensitivity_df.loc[top_indices]
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    rank_matrix = top_data[rank_cols].values
    
    im = ax.imshow(rank_matrix, aspect='auto', cmap='RdYlGn_r')
    
    ax.set_xticks(range(len(rank_cols)))
    ax.set_xticklabels([col.replace('rank_', 'α=') for col in rank_cols], rotation=45)
    ax.set_yticks(range(len(top_data)))
    ax.set_yticklabels([f"Node {node}" for node in top_data['node']])
    
    ax.set_xlabel('Damping Factor', fontsize=12)
    ax.set_ylabel('Node', fontsize=12)
    ax.set_title(f'Top {top_n} Nodes: Rank Sensitivity to α', fontsize=14)
    
    plt.colorbar(im, ax=ax, label='Rank')
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig
