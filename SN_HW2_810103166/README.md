# Social Networks - Homework 2

**Student:** Erfan Shahabi  
**Student ID:** 810103166  
**University:** University of Tehran

## Structure
```
SN_HW2_810103166/
├── data/
│   ├── politician.edges.csv
│   ├── politician.nodes.csv
│   └── Wiki-Vote.txt
├── src/
│   ├── question1/
│   │   ├── centrality.py
│   │   ├── analysis.py
│   │   ├── bottlenecks.py
│   │   ├── efficiency.py
│   │   ├── bonacich.py
│   │   └── visualization.py
│   └── question2/
│       ├── ranking.py
│       ├── analysis.py
│       ├── stability.py
│       └── visualization.py
├── notebooks/
│   ├── question1_analysis.ipynb
│   └── question2_analysis.ipynb
├── results/
│   └── plots/
└── tests/
```

## Setup
```bash
pip install -r requirements.txt
```

## Question 1: Political Power Network Analysis

**Dataset:** Wiki-Vote (5,696 politicians, 36,836 edges)

**Run:**
```bash
cd notebooks
jupyter notebook question1_analysis.ipynb
```

**Outputs:**
- Centrality rankings (degree, eigenvector, closeness)
- Gap analysis plots
- Hub anomaly identification
- Betweenness centrality analysis
- Efficient monitors identification
- Bonacich power trajectories

## Question 2: Ranking Algorithms Comparison

**Dataset:** Wiki-Vote (7,066 nodes)

**Run:**
```bash
cd notebooks
jupyter notebook question2_analysis.ipynb
```

**Outputs:**
- HITS vs PageRank comparison scatter plot
- Divergent nodes analysis
- PageRank stability trajectories
- Sensitivity heatmap

## Requirements

- Python 3.8+
- networkx
- numpy
- pandas
- matplotlib
- jupyter

## Reports

Complete analysis reports available in Word format:
- SN_HW2_810103166.pdf
