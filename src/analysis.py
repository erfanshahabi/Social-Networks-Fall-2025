import networkx as nx
import numpy as np


def calculate_average_shortest_path(G, sample_size=5000):
    if not nx.is_connected(G):
        largest_cc = max(nx.connected_components(G), key=len)
        G = G.subgraph(largest_cc).copy()
    
    N = G.number_of_nodes()
    
    if N <= 1000:
        return nx.average_shortest_path_length(G)
    
    nodes = list(G.nodes())
    path_lengths = []
    
    for _ in range(sample_size):
        source = np.random.choice(nodes)
        target = np.random.choice(nodes)
        
        if source != target:
            try:
                length = nx.shortest_path_length(G, source, target)
                path_lengths.append(length)
            except nx.NetworkXNoPath:
                continue
    
    return np.mean(path_lengths) if path_lengths else np.nan


def run_simulation(N_values):
    from .networks import (create_1d_lattice, create_2d_lattice, 
                          create_3d_lattice, create_random_network)
    
    results = {
        '1D Lattice': {'N': [], 'd': []},
        '2D Lattice': {'N': [], 'd': []},
        '3D Lattice': {'N': [], 'd': []},
        'Random Network': {'N': [], 'd': []}
    }
    
    for N in N_values:
        print(f"Processing N = {N}")
        
        G_1d = create_1d_lattice(N, k=2)
        if nx.is_connected(G_1d):
            d_1d = calculate_average_shortest_path(G_1d, sample_size=5000)
            results['1D Lattice']['N'].append(N)
            results['1D Lattice']['d'].append(d_1d)
        
        side_2d = int(np.sqrt(N))
        actual_N_2d = side_2d ** 2
        if abs(actual_N_2d - N) < 100:
            G_2d, actual_N_2d = create_2d_lattice(N)
            if nx.is_connected(G_2d):
                d_2d = calculate_average_shortest_path(G_2d, sample_size=5000)
                results['2D Lattice']['N'].append(actual_N_2d)
                results['2D Lattice']['d'].append(d_2d)
        
        side_3d = int(np.cbrt(N))
        actual_N_3d = side_3d ** 3
        if abs(actual_N_3d - N) < 200:
            G_3d, actual_N_3d = create_3d_lattice(N)
            if nx.is_connected(G_3d):
                d_3d = calculate_average_shortest_path(G_3d, sample_size=5000)
                results['3D Lattice']['N'].append(actual_N_3d)
                results['3D Lattice']['d'].append(d_3d)
        
        G_rn = create_random_network(N)
        if nx.is_connected(G_rn):
            d_rn = calculate_average_shortest_path(G_rn, sample_size=5000)
            results['Random Network']['N'].append(N)
            results['Random Network']['d'].append(d_rn)
    
    return results


def calculate_scaling_exponents(results):
    exponents = {}
    
    for network_type, data in results.items():
        if len(data['N']) > 2:
            N_arr = np.array(data['N'])
            d_arr = np.array(data['d'])
            
            log_N = np.log(N_arr)
            log_d = np.log(d_arr)
            coeffs = np.polyfit(log_N, log_d, 1)
            exponent = coeffs[0]
            
            exponents[network_type] = exponent
    
    return exponents