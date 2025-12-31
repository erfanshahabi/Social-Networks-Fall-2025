import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def plot_scaling_results(results, save_path='results/plots/scaling_behavior.png'):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    colors = {
        '1D Lattice': 'blue',
        '2D Lattice': 'green',
        '3D Lattice': 'orange',
        'Random Network': 'red'
    }
    
    def linear(N, a):
        return a * N
    
    def sqrt(N, a):
        return a * np.sqrt(N)
    
    def cbrt(N, a):
        return a * np.cbrt(N)
    
    def log(N, a):
        return a * np.log(N)
    
    for network_type, data in results.items():
        if len(data['N']) > 0:
            N_arr = np.array(data['N'])
            d_arr = np.array(data['d'])
            
            ax1.scatter(N_arr, d_arr, label=network_type, 
                       color=colors[network_type], s=50, alpha=0.7)
            
            if network_type == '1D Lattice' and len(N_arr) > 1:
                try:
                    popt, _ = curve_fit(linear, N_arr, d_arr)
                    N_fit = np.linspace(min(N_arr), max(N_arr), 100)
                    ax1.plot(N_fit, linear(N_fit, *popt), '--', 
                            color=colors[network_type], alpha=0.5)
                except:
                    pass
            elif network_type == '2D Lattice' and len(N_arr) > 1:
                try:
                    popt, _ = curve_fit(sqrt, N_arr, d_arr)
                    N_fit = np.linspace(min(N_arr), max(N_arr), 100)
                    ax1.plot(N_fit, sqrt(N_fit, *popt), '--', 
                            color=colors[network_type], alpha=0.5)
                except:
                    pass
            elif network_type == '3D Lattice' and len(N_arr) > 1:
                try:
                    popt, _ = curve_fit(cbrt, N_arr, d_arr)
                    N_fit = np.linspace(min(N_arr), max(N_arr), 100)
                    ax1.plot(N_fit, cbrt(N_fit, *popt), '--', 
                            color=colors[network_type], alpha=0.5)
                except:
                    pass
            elif network_type == 'Random Network' and len(N_arr) > 1:
                try:
                    popt, _ = curve_fit(log, N_arr, d_arr)
                    N_fit = np.linspace(min(N_arr), max(N_arr), 100)
                    ax1.plot(N_fit, log(N_fit, *popt), '--', 
                            color=colors[network_type], alpha=0.5)
                except:
                    pass
    
    ax1.set_xlabel('Network Size (N)', fontsize=12)
    ax1.set_ylabel('Average Shortest Path Length <d>', fontsize=12)
    ax1.set_title('Scaling Behavior: Linear Scale', fontsize=14)
    ax1.legend(fontsize=9)
    ax1.grid(True, alpha=0.3)
    
    for network_type, data in results.items():
        if len(data['N']) > 0:
            N_arr = np.array(data['N'])
            d_arr = np.array(data['d'])
            ax2.scatter(N_arr, d_arr, label=network_type, 
                       color=colors[network_type], s=50, alpha=0.7)
    
    ax2.set_xlabel('Network Size (N)', fontsize=12)
    ax2.set_ylabel('Average Shortest Path Length <d>', fontsize=12)
    ax2.set_title('Scaling Behavior: Log-Log Scale', fontsize=14)
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3, which='both')
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Plot saved to {save_path}")
    
    return fig