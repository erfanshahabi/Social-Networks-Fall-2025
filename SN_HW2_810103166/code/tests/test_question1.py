import pytest
import networkx as nx
from src.question1.centrality import *
from src.question1.analysis import *


def test_normalized_degree():
    G = nx.karate_club_graph()
    degrees = calculate_normalized_degree(G)
    
    assert len(degrees) == G.number_of_nodes()
    assert all(0 <= v <= 1 for v in degrees.values())


def test_eigenvector_centrality():
    G = nx.karate_club_graph()
    eig = calculate_eigenvector_centrality(G)
    
    assert len(eig) == G.number_of_nodes()
    assert all(v >= 0 for v in eig.values())


def test_closeness_centrality():
    G = nx.karate_club_graph()
    close = calculate_closeness_centrality(G)
    
    assert len(close) == G.number_of_nodes()
    assert all(0 < v <= 1 for v in close.values())


def test_gap_analysis():
    G = nx.karate_club_graph()
    centralities = calculate_all_centralities(G)
    df = gap_analysis(centralities)
    
    assert len(df) == G.number_of_nodes()
    assert 'degree_rank' in df.columns
    assert 'eig_rank' in df.columns
