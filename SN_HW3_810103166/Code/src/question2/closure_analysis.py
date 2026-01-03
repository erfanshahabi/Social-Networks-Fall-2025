import networkx as nx


def find_triadic_closures(G_old, G_new):
    """Find triadic closure events (friend of friend becomes friend)"""
    triadic_closures = []
    
    new_edges = set(G_new.edges()) - set(G_old.edges())
    
    for u, v in new_edges:
        if u in G_old and v in G_old:
            # Check if u and v have common neighbors in old network
            neighbors_u = set(G_old.neighbors(u))
            neighbors_v = set(G_old.neighbors(v))
            common = neighbors_u & neighbors_v
            
            if len(common) > 0:
                triadic_closures.append({
                    'u': u,
                    'v': v,
                    'common_friends': list(common),
                    'u_smokes': G_new.nodes[u].get('smokes', 0),
                    'v_smokes': G_new.nodes[v].get('smokes', 0)
                })
    
    return triadic_closures


def find_focal_closures_smoking(G_old, G_new):
    """Find focal closure: new connections between smokers"""
    new_edges = set(G_new.edges()) - set(G_old.edges())
    
    focal_closures = []
    for u, v in new_edges:
        u_smokes = G_new.nodes[u].get('smokes', 0)
        v_smokes = G_new.nodes[v].get('smokes', 0)
        
        if u_smokes == 1 and v_smokes == 1:
            focal_closures.append({
                'u': u,
                'v': v,
                'type': 'both_smokers'
            })
    
    return focal_closures


def find_membership_closures(G_old, G_new):
    """Find closure within same class"""
    new_edges = set(G_new.edges()) - set(G_old.edges())
    
    membership_closures = []
    for u, v in new_edges:
        class_u = G_new.nodes[u].get('class_number')
        class_v = G_new.nodes[v].get('class_number')
        
        if class_u == class_v:
            membership_closures.append({
                'u': u,
                'v': v,
                'class': class_u
            })
    
    return membership_closures


def analyze_closures_over_time(networks):
    """Analyze all closure types over time"""
    days = [1, 30, 60, 90]
    results = {}
    
    for i in range(len(days) - 1):
        day_old = days[i]
        day_new = days[i + 1]
        
        G_old = networks[day_old]
        G_new = networks[day_new]
        
        period = f"Day {day_old} → Day {day_new}"
        
        triadic = find_triadic_closures(G_old, G_new)
        focal = find_focal_closures_smoking(G_old, G_new)
        membership = find_membership_closures(G_old, G_new)
        
        # Count smokers involved in triadic closure
        smoker_triadic = sum(1 for t in triadic if t['u_smokes'] == 1 or t['v_smokes'] == 1)
        
        results[period] = {
            'triadic_closures': len(triadic),
            'triadic_with_smokers': smoker_triadic,
            'focal_closures_smoking': len(focal),
            'membership_closures': len(membership),
            'total_new_edges': G_new.number_of_edges() - G_old.number_of_edges()
        }
    
    return results
