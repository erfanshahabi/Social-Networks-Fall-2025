import numpy as np
import pandas as pd


def gap_analysis(centralities):
    degree = centralities['degree']
    eigenvector = centralities['eigenvector']
    
    df = pd.DataFrame({
        'node': list(degree.keys()),
        'degree': list(degree.values()),
        'eigenvector': list(eigenvector.values())
    })
    
    df['degree_rank'] = df['degree'].rank(ascending=False)
    df['eig_rank'] = df['eigenvector'].rank(ascending=False)
    
    return df.sort_values('eigenvector', ascending=False)


def identify_hub_anomalies(centralities, degree_threshold=100, eig_threshold=50):
    degree = centralities['degree']
    eigenvector = centralities['eigenvector']
    closeness = centralities['closeness']
    
    df = pd.DataFrame({
        'node': list(degree.keys()),
        'degree': list(degree.values()),
        'eigenvector': list(eigenvector.values()),
        'closeness': list(closeness.values())
    })
    
    df['degree_rank'] = df['degree'].rank(ascending=False)
    df['eig_rank'] = df['eigenvector'].rank(ascending=False)
    df['close_rank'] = df['closeness'].rank(ascending=False)
    
    anomalies = df[
        (df['degree_rank'] > degree_threshold) & 
        (df['eig_rank'] <= eig_threshold)
    ]
    
    return anomalies.sort_values('eig_rank')
