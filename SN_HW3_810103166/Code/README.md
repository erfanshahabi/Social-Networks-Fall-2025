**Student:** Erfan Shahabi  
**Student ID:** 810103166  
**Course:** Social Networks (Fall 2025)  
**University of Tehran**

---

## Overview

This homework analyzes social network structures through balance theory, clustering mechanisms, and temporal network evolution.

---

## Project Structure

```
SN_HW3_810103166/
├── src/
│   ├── question1/           # Balance & clustering implementation
│   │   ├── sign_prediction.py
│   │   ├── balance_test.py
│   │   ├── clusterability.py
│   │   ├── line_index.py
│   │   └── transitivity.py
│   └── question2/           # Network evolution analysis
│       ├── network_loader.py
│       ├── closure_analysis.py
│       ├── smoker_analysis.py
│       └── centrality.py
├── notebooks/
│   ├── question1_analysis.ipynb
│   └── question2_analysis.ipynb
├── Networks/
│   ├── Part_A/              # Question 1 datasets
│   └── Part_B/              # Question 2 datasets
└── results/
    ├── Question1_Final_Report.docx
    └── Question2_Report.docx
```

---

## Requirements

```
networkx>=3.0
pandas>=2.0
numpy>=1.24
matplotlib>=3.7
```

---

## Usage

### Question 1

```python
from src.question1 import (
    run_sign_prediction,
    test_balance,
    detect_clusters,
    run_line_index_analysis,
    analyze_transitivity
)

# Run analysis
run_sign_prediction('Networks/Part_A/1/balanced_graph.csv')
test_balance('Networks/Part_A/2/network_a.csv')
detect_clusters('Networks/Part_A/3/network_a.csv')
```

### Question 2

```python
from src.question2 import (
    load_all_networks,
    analyze_closures_over_time,
    compare_smokers_nonsmokers,
    get_top_central_students
)

# Load data
networks, properties = load_all_networks()

# Analyze closures
results = analyze_closures_over_time(networks)

# Compare groups
comparison = compare_smokers_nonsmokers(properties)
```

---


## License

Academic use only - University of Tehran, Fall 2025