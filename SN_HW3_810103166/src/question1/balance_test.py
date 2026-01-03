import networkx as nx
import pandas as pd


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


def find_supernodes(G, edge_signs):
    G_pos = nx.Graph()
    G_pos.add_nodes_from(G.nodes())
    
    for (u, v), sign in edge_signs.items():
        if sign == 1:
            G_pos.add_edge(u, v)
    
    components = list(nx.connected_components(G_pos))
    
    node_to_supernode = {}
    for i, comp in enumerate(components):
        for node in comp:
            node_to_supernode[node] = i
    
    return components, node_to_supernode


def build_reduced_graph(G, edge_signs, components, node_to_supernode):
    G_reduced = nx.Graph()
    G_reduced.add_nodes_from(range(len(components)))
    
    for (u, v), sign in edge_signs.items():
        su = node_to_supernode[u]
        sv = node_to_supernode[v]
        
        if su != sv and sign == -1:
            G_reduced.add_edge(su, sv)
    
    return G_reduced


def is_balanced(G_reduced):
    if G_reduced.number_of_edges() == 0:
        return True
    
    return nx.is_bipartite(G_reduced)


def test_balance(filepath):
    print(f"\nTesting: {filepath.split('/')[-1]}")
    G, edge_signs = load_signed_network(filepath)
    
    print(f"Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")
    
    components, node_to_supernode = find_supernodes(G, edge_signs)
    print(f"Supernodes: {len(components)}")
    
    for i, comp in enumerate(components[:5]):
        nodes = sorted(list(comp))
        if len(nodes) > 5:
            print(f"  S{i}: {nodes[:5]} ... ({len(nodes)} nodes)")
        else:
            print(f"  S{i}: {nodes}")
    
    if len(components) > 5:
        print(f"  ... and {len(components) - 5} more supernodes")
    
    G_reduced = build_reduced_graph(G, edge_signs, components, node_to_supernode)
    balanced = is_balanced(G_reduced)
    
    print(f"\nResult: {'✓ BALANCED' if balanced else '✗ UNBALANCED'}")
    
    return balanced, node_to_supernode
