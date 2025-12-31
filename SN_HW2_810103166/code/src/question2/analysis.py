import pandas as pd
import numpy as np


def ranking_comparison(hits_authorities, pagerank_scores):
    hits_ranks = pd.DataFrame(list(hits_authorities.items()), columns=['node', 'authority_score'])
    hits_ranks['authority_rank'] = hits_ranks['authority_score'].rank(ascending=False)
    
    pr_ranks = pd.DataFrame(list(pagerank_scores.items()), columns=['node', 'pagerank_score'])
    pr_ranks['pagerank_rank'] = pr_ranks['pagerank_score'].rank(ascending=False)
    
    comparison = hits_ranks.merge(pr_ranks, on='node')
    comparison['rank_diff'] = abs(comparison['authority_rank'] - comparison['pagerank_rank'])
    
    return comparison.sort_values('rank_diff', ascending=False)


def identify_divergent_nodes(comparison_df, threshold_percentile=95):
    threshold = np.percentile(comparison_df['rank_diff'], threshold_percentile)
    divergent = comparison_df[comparison_df['rank_diff'] >= threshold]
    return divergent.sort_values('rank_diff', ascending=False)
