import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def simulate_erdos_renyi_evolution(N, k, num_realizations=50):
    p = k / (N - 1)
    
    results = {
        'giant_component_size': [],
        'order_parameter': [],
        'avg_small_cluster_size': []
    }
    
    for _ in range(num_realizations):
        G = nx.erdos_renyi_graph(N, p)
        
        components = list(nx.connected_components(G))
        component_sizes = [len(c) for c in components]
        
        if len(component_sizes) > 0:
            largest_size = max(component_sizes)
            results['giant_component_size'].append(largest_size)
            results['order_parameter'].append(largest_size / N)
            
            small_clusters = [s for s in component_sizes if s != largest_size]
            if len(small_clusters) > 0:
                avg_small = np.mean(small_clusters)
            else:
                avg_small = 0
            results['avg_small_cluster_size'].append(avg_small)
        else:
            results['giant_component_size'].append(0)
            results['order_parameter'].append(0)
            results['avg_small_cluster_size'].append(0)
    
    return {
        'giant_component_size': np.mean(results['giant_component_size']),
        'order_parameter': np.mean(results['order_parameter']),
        'avg_small_cluster_size': np.mean(results['avg_small_cluster_size'])
    }


def phase_transition_analysis(N=1000, k_min=0, k_max=5, step_coarse=0.1, 
                              step_fine=0.02, critical_window=(0.8, 1.2), 
                              num_realizations=50):
    k_values = []
    order_params = []
    avg_cluster_sizes = []
    
    current_k = k_min
    while current_k <= k_max:
        if critical_window[0] <= current_k <= critical_window[1]:
            step = step_fine
        else:
            step = step_coarse
        
        k_values.append(current_k)
        
        results = simulate_erdos_renyi_evolution(N, current_k, num_realizations)
        order_params.append(results['order_parameter'])
        avg_cluster_sizes.append(results['avg_small_cluster_size'])
        
        current_k += step
    
    return {
        'k_values': np.array(k_values),
        'order_parameter': np.array(order_params),
        'avg_cluster_size': np.array(avg_cluster_sizes)
    }


def plot_phase_transition(results, save_path='results/plots/phase_transition.png'):
    import os
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    k_values = results['k_values']
    order_param = results['order_parameter']
    avg_cluster = results['avg_cluster_size']
    
    ax1.plot(k_values, order_param, 'b-', linewidth=2)
    ax1.axvline(x=1.0, color='r', linestyle='--', label='Theoretical critical point <k>=1')
    ax1.set_xlabel('Average Degree <k>', fontsize=12)
    ax1.set_ylabel('Order Parameter S = N_G/N', fontsize=12)
    ax1.set_title('Giant Component Size vs Average Degree', fontsize=14)
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    ax2.plot(k_values, avg_cluster, 'g-', linewidth=2)
    ax2.axvline(x=1.0, color='r', linestyle='--', label='Theoretical critical point <k>=1')
    ax2.set_xlabel('Average Degree <k>', fontsize=12)
    ax2.set_ylabel('Average Size of Small Clusters <s>', fontsize=12)
    ax2.set_title('Small Cluster Size vs Average Degree', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig


def finite_size_analysis(k_values, N_values, num_realizations=50):
    results = {}
    
    for N in N_values:
        order_params = []
        
        for k in k_values:
            result = simulate_erdos_renyi_evolution(N, k, num_realizations)
            order_params.append(result['order_parameter'])
        
        results[N] = np.array(order_params)
    
    return results


def plot_finite_size_effects(k_values, finite_size_results, save_path='results/plots/finite_size_effects.png'):
    import os
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = ['blue', 'green', 'red']
    
    for i, (N, order_params) in enumerate(finite_size_results.items()):
        ax.plot(k_values, order_params, '-o', color=colors[i], 
                linewidth=2, markersize=4, label=f'N = {N}')
    
    ax.axvline(x=1.0, color='black', linestyle='--', 
               label='Theoretical critical point <k>=1', linewidth=2)
    ax.set_xlabel('Average Degree <k>', fontsize=12)
    ax.set_ylabel('Order Parameter S = N_G/N', fontsize=12)
    ax.set_title('Finite Size Effects on Phase Transition', fontsize=14)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=11)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig


def analyze_transition_sharpness(k_values, finite_size_results):
    sharpness = {}
    
    for N, order_params in finite_size_results.items():
        critical_idx = np.argmin(np.abs(k_values - 1.0))
        
        if critical_idx > 0 and critical_idx < len(k_values) - 1:
            slope = (order_params[critical_idx + 1] - order_params[critical_idx - 1]) / \
                    (k_values[critical_idx + 1] - k_values[critical_idx - 1])
            sharpness[N] = slope
        else:
            sharpness[N] = 0
    
    return sharpness


def analyze_divergence_at_criticality(N_values, k_critical=1.0, k_range=0.3, num_points=20, num_realizations=50):
    results = {}
    
    k_values = np.linspace(k_critical - k_range, k_critical + k_range, num_points)
    
    for N in N_values:
        order_params = []
        avg_clusters = []
        
        for k in k_values:
            result = simulate_erdos_renyi_evolution(N, k, num_realizations)
            order_params.append(result['order_parameter'])
            avg_clusters.append(result['avg_small_cluster_size'])
        
        results[N] = {
            'k_values': k_values,
            'order_parameter': np.array(order_params),
            'avg_cluster_size': np.array(avg_clusters)
        }
    
    return results


def plot_divergence_analysis(divergence_results, save_path='results/plots/divergence_analysis.png'):
    import os
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    colors = ['blue', 'green', 'red']
    N_values = list(divergence_results.keys())
    
    for i, N in enumerate(N_values):
        data = divergence_results[N]
        k_vals = data['k_values']
        avg_cluster = data['avg_cluster_size']
        
        ax1.plot(k_vals, avg_cluster, '-o', color=colors[i], 
                linewidth=2, markersize=4, label=f'N = {N}')
    
    ax1.axvline(x=1.0, color='black', linestyle='--', linewidth=2, label='<k> = 1')
    ax1.set_xlabel('Average Degree <k>', fontsize=12)
    ax1.set_ylabel('Average Cluster Size <s>', fontsize=12)
    ax1.set_title('Divergence at Critical Point', fontsize=14)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    max_cluster_sizes = []
    for N in N_values:
        data = divergence_results[N]
        max_cluster_sizes.append(np.max(data['avg_cluster_size']))
    
    ax2.plot(N_values, max_cluster_sizes, 'ro-', linewidth=2, markersize=8)
    ax2.set_xlabel('Network Size N', fontsize=12)
    ax2.set_ylabel('Max Average Cluster Size', fontsize=12)
    ax2.set_title('Peak Cluster Size vs Network Size', fontsize=14)
    ax2.grid(True, alpha=0.3)
    ax2.set_xscale('log')
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig


def calculate_giant_component_scaling(N_values, k_values_near_critical, num_realizations=50):
    scaling_results = {}
    
    for k in k_values_near_critical:
        giant_sizes = []
        
        for N in N_values:
            result = simulate_erdos_renyi_evolution(N, k, num_realizations)
            giant_sizes.append(result['order_parameter'])
        
        scaling_results[k] = np.array(giant_sizes)
    
    return scaling_results


def plot_giant_component_scaling(N_values, scaling_results, save_path='results/plots/giant_component_scaling.png'):
    import os
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    for k, giant_sizes in scaling_results.items():
        ax.plot(N_values, giant_sizes, '-o', linewidth=2, markersize=6, label=f'<k> = {k:.2f}')
    
    ax.set_xlabel('Network Size N', fontsize=12)
    ax.set_ylabel('Relative Giant Component Size S', fontsize=12)
    ax.set_title('Giant Component Scaling with Network Size', fontsize=14)
    ax.set_xscale('log')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig