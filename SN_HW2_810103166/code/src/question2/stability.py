import networkx as nx
import pandas as pd
import numpy as np


def pagerank_sensitivity_analysis(G, alpha_values=None):
    if alpha_values is None:
        alpha_values = np.linspace(0.50, 0.85, 8)
    
    results = {}
    
    for alpha in alpha_values:
        pr = nx.pagerank(G, alpha=alpha)
        df = pd.DataFrame(list(pr.items()), columns=['node', f'score_{alpha:.2f}'])
        df[f'rank_{alpha:.2f}'] = df[f'score_{alpha:.2f}'].rank(ascending=False)
        results[alpha] = df
    
    merged = results[alpha_values[0]][['node']]
    for alpha in alpha_values:
        merged = merged.merge(results[alpha], on='node')
    
    return merged


def analyze_rank_trajectories(sensitivity_df, top_n=10):
    rank_cols = [col for col in sensitivity_df.columns if 'rank_' in col]
    
    avg_ranks = sensitivity_df[rank_cols].mean(axis=1)
    top_nodes = sensitivity_df.loc[avg_ranks.nsmallest(top_n).index]
    
    trajectories = top_nodes[['node'] + rank_cols].copy()
    
    return trajectories
