import networkx as nx
import numpy as np
import pandas as pd


def calculate_hits(G, max_iter=100, tol=1e-8):
    hubs, authorities = nx.hits(G, max_iter=max_iter, tol=tol)
    return hubs, authorities


def calculate_pagerank(G, alpha=0.85, max_iter=100, tol=1e-8):
    pagerank = nx.pagerank(G, alpha=alpha, max_iter=max_iter, tol=tol)
    return pagerank


def scores_to_ranks(scores_dict):
    df = pd.DataFrame(list(scores_dict.items()), columns=['node', 'score'])
    df['rank'] = df['score'].rank(ascending=False)
    return df.set_index('node')['rank'].to_dict()
