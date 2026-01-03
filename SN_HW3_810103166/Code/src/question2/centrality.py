import networkx as nx


def compute_degree_centrality(G):
    """Compute degree centrality for all nodes"""
    centrality = nx.degree_centrality(G)
    return centrality


def get_top_central_students(G, top_n=5):
    """Get top N most central students"""
    centrality = compute_degree_centrality(G)
    
    sorted_nodes = sorted(centrality.items(), key=lambda x: x[1], reverse=True)
    
    top_students = []
    for node, cent in sorted_nodes[:top_n]:
        top_students.append({
            'student_id': node,
            'centrality': cent,
            'degree': G.degree(node),
            'smokes': G.nodes[node].get('smokes', 0),
            'gender': G.nodes[node].get('gender', -1),
            'class': G.nodes[node].get('class_number', -1)
        })
    
    return top_students


def analyze_central_students_role(G, top_students):
    """Analyze role of central students"""
    analysis = []
    
    for student in top_students:
        node = student['student_id']
        neighbors = list(G.neighbors(node))
        
        smoker_neighbors = sum(1 for n in neighbors if G.nodes[n].get('smokes', 0) == 1)
        
        analysis.append({
            'student_id': node,
            'total_connections': len(neighbors),
            'smoker_connections': smoker_neighbors,
            'is_smoker': student['smokes'],
            'influence_potential': smoker_neighbors / len(neighbors) if len(neighbors) > 0 else 0
        })
    
    return analysis
