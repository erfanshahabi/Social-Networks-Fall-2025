import networkx as nx
import pandas as pd
from collections import deque


def load_signed_graph(filepath):
    df = pd.read_csv(filepath)
    G = nx.Graph()
    edge_signs = {}
    
    for _, row in df.iterrows():
        u, v = int(row['u']), int(row['v'])
        sign = row['sign']
        
        G.add_edge(u, v)
        
        # 0 means unknown
        if pd.isna(sign) or sign == 0:
            edge_signs[(min(u,v), max(u,v))] = None
        else:
            edge_signs[(min(u,v), max(u,v))] = int(sign)
    
    return G, edge_signs


def predict_sign_iterative(G, edge_signs):
    """Iteratively predict signs using balance property"""
    predictions = {}
    changed = True
    iterations = 0
    max_iterations = 100
    
    while changed and iterations < max_iterations:
        changed = False
        iterations += 1
        
        # Try all triangles
        for node in G.nodes():
            neighbors = list(G.neighbors(node))
            
            for i in range(len(neighbors)):
                for j in range(i+1, len(neighbors)):
                    n1, n2 = neighbors[i], neighbors[j]
                    
                    # Get edges in triangle
                    e1 = (min(node, n1), max(node, n1))
                    e2 = (min(node, n2), max(node, n2))
                    e3 = (min(n1, n2), max(n1, n2))
                    
                    signs = [edge_signs.get(e1), edge_signs.get(e2), edge_signs.get(e3)]
                    
                    # Count known signs
                    known_count = sum(1 for s in signs if s is not None)
                    
                    # If exactly 2 are known, predict the third
                    if known_count == 2:
                        for idx, (edge, sign) in enumerate([(e1, signs[0]), (e2, signs[1]), (e3, signs[2])]):
                            if sign is None:
                                other_signs = [signs[k] for k in range(3) if k != idx and signs[k] is not None]
                                # Balance: product of all three signs should be +1
                                predicted = other_signs[0] * other_signs[1]
                                edge_signs[edge] = predicted
                                predictions[edge] = predicted
                                changed = True
    
    return predictions


def run_sign_prediction(filepath):
    print(f"Loading: {filepath}")
    G, edge_signs = load_signed_graph(filepath)
    
    print(f"Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")
    
    unknown = [(u,v) for (u,v), s in edge_signs.items() if s is None]
    print(f"Unknown edges: {len(unknown)}")
    
    predictions = predict_sign_iterative(G, edge_signs)
    
    print(f"\nPredicted {len(predictions)} unknown edges:")
    
    count = 0
    for (u, v), sign in sorted(predictions.items()):
        print(f"  {u}-{v}: {'+' if sign == 1 else '-'}")
        count += 1
        if count >= 20:
            print(f"  ... and {len(predictions) - 20} more")
            break
    
    remaining_unknown = sum(1 for s in edge_signs.values() if s is None)
    if remaining_unknown > 0:
        print(f"\nCould not predict {remaining_unknown} edges (not enough constraints)")
    
    return predictions
