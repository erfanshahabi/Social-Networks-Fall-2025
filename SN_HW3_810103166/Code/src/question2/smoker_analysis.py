import pandas as pd
import numpy as np


def compare_smokers_nonsmokers(properties):
    """Compare feature distributions"""
    days = [1, 30, 60, 90]
    
    comparison = {}
    
    for day in days:
        df = properties[day]
        
        smokers = df[df['smokes'] == 1]
        non_smokers = df[df['smokes'] == 0]
        
        comparison[f'Day {day}'] = {
            'n_smokers': len(smokers),
            'n_non_smokers': len(non_smokers),
            'smokers_male': (smokers['gender'] == 1).sum(),
            'nonsmokers_male': (non_smokers['gender'] == 1).sum(),
            'smokers_avg_age': smokers['age'].mean(),
            'nonsmokers_avg_age': non_smokers['age'].mean(),
            'smokers_avg_studies': smokers['studies'].mean(),
            'nonsmokers_avg_studies': non_smokers['studies'].mean(),
            'smokers_football': (smokers['plays_football'] == 1).sum(),
            'nonsmokers_football': (non_smokers['plays_football'] == 1).sum(),
            'smokers_movies': (smokers['watches_movies'] == 1).sum(),
            'nonsmokers_movies': (non_smokers['watches_movies'] == 1).sum(),
            'smokers_club': (smokers['club'] == 1).sum(),
            'nonsmokers_club': (non_smokers['club'] == 1).sum()
        }
    
    return comparison


def track_smoking_evolution(properties):
    """Track how smoking behavior changes"""
    days = [1, 30, 60, 90]
    
    evolution = {}
    
    for day in days:
        df = properties[day]
        smoker_count = (df['smokes'] == 1).sum()
        evolution[f'Day {day}'] = smoker_count
    
    return evolution
