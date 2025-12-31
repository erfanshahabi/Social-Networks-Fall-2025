import networkx as nx
import pandas as pd


def calculate_betweenness_centrality(G):
    return nx.betweenness_centrality(G, normalized=True)


def rank_gap_analysis(G, top_n=10):
    betweenness = calculate_betweenness_centrality(G)
    degree = dict(G.degree())
    closeness = nx.closeness_centrality(G)
    
    df = pd.DataFrame({
        'node': list(betweenness.keys()),
        'betweenness': list(betweenness.values()),
        'degree': [degree[n] for n in betweenness.keys()],
        'closeness': [closeness[n] for n in betweenness.keys()]
    })
    
    df['bet_rank'] = df['betweenness'].rank(ascending=False)
    df['deg_rank'] = df['degree'].rank(ascending=False)
    df['close_rank'] = df['closeness'].rank(ascending=False)
    
    top_betweenness = df.nsmallest(top_n, 'bet_rank')
    
    return top_betweenness
