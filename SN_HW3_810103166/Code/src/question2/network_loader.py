import networkx as nx
import pandas as pd


def load_network(day, data_path='../Networks/Part_B'):
    """Load network and attributes for a specific day"""
    
    # Load connections
    conn_file = f"{data_path}/connections_day_{day}.csv"
    edges_df = pd.read_csv(conn_file)
    
    # Create graph
    G = nx.Graph()
    for _, row in edges_df.iterrows():
        G.add_edge(int(row['node_i']), int(row['node_j']))
    
    # Load properties
    prop_file = f"{data_path}/properties_day_{day}.csv"
    props_df = pd.read_csv(prop_file)
    
    # Convert gender to binary
    props_df['gender'] = props_df['gender'].apply(lambda x: 1 if x == 'boy' else 0)
    
    # Add node attributes
    for _, row in props_df.iterrows():
        node_id = int(row['id'])
        if node_id not in G.nodes():
            G.add_node(node_id)
        
        for col in props_df.columns:
            if col != 'id':
                G.nodes[node_id][col] = row[col]
    
    return G, props_df


def load_all_networks(data_path='../Networks/Part_B'):
    """Load all 4 time steps"""
    days = [1, 30, 60, 90]
    networks = {}
    properties = {}
    
    for day in days:
        G, props = load_network(day, data_path)
        networks[day] = G
        properties[day] = props
    
    return networks, properties


def get_smokers(G):
    """Get list of smokers from network"""
    return [n for n, d in G.nodes(data=True) if d.get('smokes', 0) == 1]


def get_non_smokers(G):
    """Get list of non-smokers"""
    return [n for n, d in G.nodes(data=True) if d.get('smokes', 0) == 0]
