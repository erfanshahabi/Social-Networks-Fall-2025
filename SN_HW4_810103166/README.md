# Social Network Analysis - Homework 4

**Student Number:** 810103166  
**Course:** Social Networks  
**Instructor:** Dr. Masoud Asadpour  
**Date:** February 15, 2026

## Project Structure
```
SN_HW4_810103166/
├── src/
│   ├── q4_girvan_newman.py
│   ├── q5_algorithm_comparison.py
│   └── q6_dormant_cell.py
├── figures/
│   ├── q4_girvan_newman_analysis.png
│   ├── q5_les_miserables_analysis.png
│   └── q6_dormant_cell_detection.png
├── results/
│   └── q5_algorithm_comparison.csv
└── SN_HW4_FINAL_COMPLETE_810103166.docx
```

## Requirements
```bash
pip install networkx matplotlib seaborn scikit-learn pandas numpy python-louvain
```

## Running the Code
```bash
# Question 4: Girvan-Newman Algorithm
python src/q4_girvan_newman.py

# Question 5: Algorithm Comparison
python src/q5_algorithm_comparison.py

# Question 6: Dormant Cell Detection
python src/q6_dormant_cell.py
```

## Results Summary

### Question 4: Girvan-Newman
- Accuracy: 94.12%
- Maximum Modularity: 0.3600
- Critical Edge: (2, 13)

### Question 5: Algorithm Comparison
- Best Algorithm: Louvain
- Modularity: 0.5658
- Communities Detected: 6

### Question 6: Dormant Cell Detection
- Suspected Community: 4
- Suspicion Score: 0.852/1.000
- Members: 6 characters (trial scene)

## Report

Complete analysis and visualizations in `SN_HW4_810103166.pdf`
