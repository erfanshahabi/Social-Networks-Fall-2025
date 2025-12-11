import pytest
import networkx as nx
from src.networks import (
    create_1d_lattice,
    create_2d_lattice,
    create_3d_lattice,
    create_random_network
)


def test_1d_lattice_node_count():
    G = create_1d_lattice(50, k=2)
    assert G.number_of_nodes() == 50


def test_1d_lattice_connectivity():
    G = create_1d_lattice(100, k=2)
    assert nx.is_connected(G)


def test_1d_lattice_degree():
    G = create_1d_lattice(100, k=2)
    degrees = [G.degree(node) for node in G.nodes()]
    assert all(d == 2 for d in degrees)


def test_2d_lattice_returns_perfect_square():
    G, actual_N = create_2d_lattice(100)
    assert actual_N == 100


def test_2d_lattice_connectivity():
    G, _ = create_2d_lattice(100)
    assert nx.is_connected(G)


def test_3d_lattice_returns_perfect_cube():
    G, actual_N = create_3d_lattice(125)
    assert actual_N == 125


def test_3d_lattice_connectivity():
    G, _ = create_3d_lattice(64)
    assert nx.is_connected(G)


def test_random_network_node_count():
    G = create_random_network(50)
    assert G.number_of_nodes() == 50


def test_random_network_connectivity():
    G = create_random_network(200)
    assert nx.is_connected(G)