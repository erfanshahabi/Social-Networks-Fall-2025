import networkx as nx
import pandas as pd


def load_directed_network(filepath):
    df = pd.read_csv(filepath)
    G = nx.DiGraph()
    
    for _, row in df.iterrows():
        u, v = int(row['source']), int(row['target'])
        G.add_edge(u, v)
    
    return G


def analyze_transitivity(filepath):
    print(f"\nAnalyzing: {filepath.split('/')[-1]}")
    G = load_directed_network(filepath)
    
    print(f"Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")
    
    transitive_triples = 0
    possible_triples = 0
    missing_edges = set()
    
    for node in G.nodes():
        successors = list(G.successors(node))
        
        for mid in successors:
            for end in G.successors(mid):
                if end != node:
                    possible_triples += 1
                    
                    if G.has_edge(node, end):
                        transitive_triples += 1
                    else:
                        missing_edges.add((node, end))
    
    transitivity_ratio = transitive_triples / possible_triples if possible_triples > 0 else 0
    
    print(f"\nTransitive triples: {transitive_triples}")
    print(f"Possible triples: {possible_triples}")
    print(f"Transitivity ratio: {transitivity_ratio:.4f}")
    print(f"\nMissing edges for full transitivity: {len(missing_edges)}")
    print(f"Total edges (current): {G.number_of_edges()}")
    print(f"Total edges needed: {G.number_of_edges() + len(missing_edges)}")
    
    return {
        'transitive_triples': transitive_triples,
        'possible_triples': possible_triples,
        'transitivity_ratio': transitivity_ratio,
        'missing_edges': len(missing_edges),
        'total_edges': G.number_of_edges()
    }
