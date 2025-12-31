import pytest
import networkx as nx
from src.generative_models import (
    barabasi_albert_model,
    deterministic_scale_free_construction,
    analyze_degree_distribution
)


def test_barabasi_albert_node_count():
    N = 50
    m = 3
    G = barabasi_albert_model(N, m)
    assert G.number_of_nodes() == N


def test_barabasi_albert_connectivity():
    G = barabasi_albert_model(100, 3)
    assert nx.is_connected(G)


def test_barabasi_albert_invalid_m():
    with pytest.raises(ValueError):
        barabasi_albert_model(10, 15)


def test_deterministic_scale_free_node_count():
    iterations = 10
    G = deterministic_scale_free_construction(iterations)
    assert G.number_of_nodes() == 3 + iterations


def test_deterministic_scale_free_connectivity():
    G = deterministic_scale_free_construction(20)
    assert nx.is_connected(G)


def test_analyze_degree_distribution():
    G = barabasi_albert_model(50, 2)
    stats = analyze_degree_distribution(G)
    
    assert 'min_degree' in stats
    assert 'max_degree' in stats
    assert 'avg_degree' in stats
    assert stats['min_degree'] > 0
    assert stats['max_degree'] >= stats['min_degree']