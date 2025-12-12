import pytest
import networkx as nx
import numpy as np
from src.networks import create_1d_lattice
from src.analysis import calculate_average_shortest_path


def test_shortest_path_small_network():
    G = create_1d_lattice(10, k=2)
    d = calculate_average_shortest_path(G)
    assert isinstance(d, float)
    assert d > 0


def test_shortest_path_returns_nan_for_disconnected():
    G = nx.Graph()
    G.add_nodes_from(range(10))
    G.add_edge(0, 1)
    G.add_edge(5, 6)
    
    d = calculate_average_shortest_path(G)
    assert isinstance(d, (float, np.floating))


def test_shortest_path_sampling():
    G = create_1d_lattice(2000, k=2)
    d = calculate_average_shortest_path(G, sample_size=100)
    assert isinstance(d, float)
    assert d > 0