**Student:** Erfan Shahabi  
**Student ID:** 810103166  
**Course:** Social Networks (Fall 2025)  
**University of Tehran**

---

## Overview

This homework analyzes social network structures through balance theory, clustering mechanisms, and temporal network evolution.

---

## Question 1: Balance and Clustering

**Implementation:** Python (NetworkX, Pandas, Matplotlib)

### Parts:

1. **Sign Prediction** - Iterative triangle-based inference using structural balance
2. **Balance Test** - Super-node generation and bipartiteness testing (8 networks)
3. **Clusterability** - Weakly balanced network clustering (5 networks)
4. **Line Index** - Random vs heuristic optimization (perfect score: 0.00)
5. **Transitivity** - Directed network transitivity analysis (2.14% ratio)

**Key Results:**
- Predicted 911 edge signs from 88 unknowns
- All 8 networks balanced
- Perfect clustering achieved via heuristic optimization

---

## Question 2: School Network Evolution

**Dataset:** 120 students over 90 days (Day 1, 30, 60, 90)

### Analysis:

1. **Closure Mechanisms**
   - Triadic closure: 4.9% → 106.8% → 97.3%
   - Focal closure (smoking): 459 smoker pairs
   - Membership closure: 1,043 same-class connections

2. **Smoking Spread**
   - Initial: 20 smokers → Final: 70 smokers (250% increase)
   - Smokers study less (1.09 vs 2.06 hours)
   - Network effects drive behavioral diffusion

3. **Centrality**
   - Top student: 52 connections, 71.2% smokers
   - Central nodes accelerate information spread

**Key Finding:** Smoking behavior spreads through social networks via triadic closure, focal closure, and class-based membership.

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

## Results Summary

| Metric | Question 1 | Question 2 |
|--------|-----------|-----------|
| Networks Analyzed | 13 | 4 time steps |
| Predictions Made | 911 signs | N/A |
| Balance Status | 8/8 balanced | N/A |
| Clustering Score | LI = 0.00 | N/A |
| Transitivity | 2.14% | N/A |
| Smoker Increase | N/A | +250% (20→70) |
| Top Centrality | N/A | 52 connections |

---

## License

Academic use only - University of Tehran, Fall 2025