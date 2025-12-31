import pytest
import numpy as np
from src.phase_transition import (
    simulate_erdos_renyi_evolution,
    phase_transition_analysis,
    finite_size_analysis
)


def test_simulate_erdos_renyi_basic():
    N = 100
    k = 2.0
    result = simulate_erdos_renyi_evolution(N, k, num_realizations=10)
    
    assert 'giant_component_size' in result
    assert 'order_parameter' in result
    assert 'avg_small_cluster_size' in result
    assert 0 <= result['order_parameter'] <= 1


def test_phase_transition_below_critical():
    result = simulate_erdos_renyi_evolution(100, 0.5, num_realizations=20)
    assert result['order_parameter'] < 0.5


def test_phase_transition_above_critical():
    result = simulate_erdos_renyi_evolution(500, 2.0, num_realizations=20)
    assert result['order_parameter'] > 0.5


def test_phase_transition_analysis_structure():
    results = phase_transition_analysis(N=100, k_min=0, k_max=2, 
                                       step_coarse=0.5, num_realizations=5)
    
    assert 'k_values' in results
    assert 'order_parameter' in results
    assert 'avg_cluster_size' in results
    assert len(results['k_values']) == len(results['order_parameter'])


def test_finite_size_analysis():
    k_values = np.array([0.5, 1.0, 1.5])
    N_values = [50, 100]
    
    results = finite_size_analysis(k_values, N_values, num_realizations=5)
    
    assert len(results) == len(N_values)
    for N in N_values:
        assert len(results[N]) == len(k_values)