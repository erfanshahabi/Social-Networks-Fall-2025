# Social Network Analysis - Fall 2025

## Question 1: Small World Phenomena in Random Networks

This project implements and analyzes the scaling behavior of average shortest path length in four different network topologies:
- 1D Lattice (Ring): `<d> ~ N`
- 2D Lattice (Grid): `<d> ~ N^(1/2)`
- 3D Lattice (Cubic): `<d> ~ N^(1/3)`
- Random Network (Erdős-Rényi): `<d> ~ log(N)`

## Installation

### Prerequisites
- Python 3.8+
- Git

### Setup

1. Clone the repository:
```bash
git clone <yhttps://github.com/erfanshahabi/Social-Networks-Fall-2025.git>
cd Social-Network-Fall-2025
```

2. Create and activate virtual environment:
```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```


## Project Structure
```
Social-Network-Fall-2025/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── networks.py              # Question 1: Network creation (1D, 2D, 3D, Random)
│   ├── analysis.py              # Question 1: Path length analysis
│   ├── visualization.py         # Question 1: Scaling plots
│   ├── generative_models.py     # Question 2: BA & Deterministic models
│   └── phase_transition.py      # Question 3: Phase transition analysis
├── tests/
│   ├── __init__.py
│   ├── test_networks.py         # Tests for Question 1
│   ├── test_analysis.py         # Tests for Question 1
│   ├── test_generative_models.py # Tests for Question 2
│   └── test_phase_transition.py # Tests for Question 3
├── notebooks/
│   ├── question1_analysis.ipynb # Question 1: Small world phenomena
│   ├── question2_analysis.ipynb # Question 2: Generative models
│   └── question3_analysis.ipynb # Question 3: Phase transitions
├── results/
│   └── plots/                   # All output plots
└── data/                        # Optional data files
```

## File Descriptions

### Source Code (`src/`)
- **networks.py**: Implements 4 network topologies (1D/2D/3D lattices, random networks)
- **analysis.py**: Shortest path calculations and scaling exponent analysis
- **visualization.py**: Linear and log-log plotting for scaling behavior
- **generative_models.py**: Barabási-Albert and deterministic scale-free network generation
- **phase_transition.py**: Erdős-Rényi evolution and critical point analysis

### Tests (`tests/`)
- Comprehensive unit tests for all modules
- Test connectivity, degree distributions, and analysis functions
- Run with: `pytest tests/ -v`

### Notebooks (`notebooks/`)
- Interactive analysis and visualization for each question
- Complete workflow from data generation to final plots
- Contains detailed explanations and interpretations
## Usage

### Option 1: Run from Python
```python
from src.analysis import run_simulation
from src.visualization import plot_scaling_results

N_values = [50, 100, 200, 400, 600, 800, 1000]
results = run_simulation(N_values)
plot_scaling_results(results)
```

### Option 2: Run Jupyter Notebook
```bash
jupyter notebook notebooks/question1_analysis.ipynb
```

## Running Tests
```bash
pytest tests/
```

## Results

The simulation confirms theoretical predictions:

| Network Type | Theoretical Scaling | Measured Exponent |
|--------------|-------------------|-------------------|
| 1D Lattice   | N (exponent=1.0)  | ~0.997           |
| 2D Lattice   | N^0.5             | ~0.499           |
| 3D Lattice   | N^0.333           | ~0.348           |
| Random Network | log(N)          | logarithmic      |

## Key Findings

1. **Random networks exhibit small-world property**: For N=5000, random network has <d>≈4 while 1D lattice has <d>≈1250 (312x more efficient)

2. **Dimensional constraints**: Lattices show polynomial scaling determined by dimensionality (d ~ N^(1/D))

3. **Shortcuts**: Random connections provide long-range shortcuts, reducing path length from polynomial to logarithmic
## Question 2: Generative Graph Models & Genetic Encodings

Implementation of scale-free network generation using two different approaches:

### Part (a): Network Construction
- **Barabási-Albert Model**: Stochastic preferential attachment (N nodes, m edges per node)
- **Deterministic Construction**: Deterministic scale-free network generation starting from triangle

### Part (b): Analysis
- Adjacency matrix visualization
- Degree distribution comparison
- Blockiness analysis
- Sorted adjacency matrices to reveal community structure

## Usage for Question 2

### Python
```python
from src.generative_models import barabasi_albert_model, deterministic_scale_free_construction

N = 100
m = 3

G_BA = barabasi_albert_model(N, m)
G_det = deterministic_scale_free_construction(N - 3)
```

### Jupyter Notebook
```bash
jupyter notebook notebooks/question2_analysis.ipynb
```

## Results - Question 2

Both models produce scale-free networks with power-law degree distributions, but:

| Model | Properties | Blockiness |
|-------|-----------|------------|
| Barabási-Albert | Stochastic, natural preferential attachment | Lower, more random |
| Deterministic | Predictable structure, systematic growth | Higher, more structured |

**Key Finding**: The deterministic model shows more block structure in the adjacency matrix due to its systematic construction process, while BA model has a more distributed connection pattern.

## Question 3: The Evolution of Random Networks & Phase Transitions

Implementation and analysis of phase transitions in Erdős-Rényi random networks. This question explores the emergence of a giant component as the average degree increases past the critical threshold.

### Theory

In random networks, as we increase the average degree `<k>`, the network undergoes a dramatic phase transition:
- **Subcritical regime** (`<k> < 1`): Network consists of small isolated clusters
- **Critical point** (`<k> = 1`): Phase transition occurs
- **Supercritical regime** (`<k> > 1`): Giant component emerges containing O(N) nodes

### Implementation

#### Part (a): Simulating Network Evolution
Simulate Erdős-Rényi networks with varying average degree:
- Fixed network size: N = 1000
- Variable step sizes: coarse (0.1) for non-critical regions, fine (0.02) near `<k> ∈ [0.8, 1.2]`
- Average over 50 independent realizations for smooth curves
- Track: giant component size (N_G), order parameter (S = N_G/N), average small cluster size

#### Part (b): Analyzing the Critical Threshold
Generate two key plots:
- **Plot 1**: Order parameter S vs `<k>`
- **Plot 2**: Average size of isolated clusters `<s>` vs `<k>`

Key observations:
1. **Critical point**: Transition occurs at theoretical prediction `<k> = 1`
2. **Cluster size divergence**: `<s>` peaks near critical point then decreases in supercritical regime
3. **Physical meaning**: At criticality, clusters of all sizes coexist, leading to peak in average cluster size

#### Part (c): Finite Size Effects
Compare phase transitions for different network sizes:
- Test N = 100, N = 1,000, and N = 10,000
- Plot all three on same figure

Observations:
1. **Sharpness increases with N**: Transition becomes more abrupt for larger networks
2. **At `<k> = 1`**: Giant component size S tends toward zero as N → ∞
3. **Theoretical limit**: In infinite networks (N → ∞), transition is perfectly sharp

Scaling prediction: N_G ~ N^(2/3) at criticality

#### Part (d): Divergence at Criticality
Analyze behavior of average cluster size near critical point across different network sizes.

Key findings:
- Peak in `<s>` becomes more pronounced for larger N
- Peak location converges to `<k> = 1`
- Peak height grows with N, consistent with divergence in thermodynamic limit

## Usage for Question 3

### Python
```python
from src.phase_transition import phase_transition_analysis, plot_phase_transition

# Run basic analysis
results = phase_transition_analysis(
    N=1000,
    k_min=0,
    k_max=5,
    step_coarse=0.1,
    step_fine=0.02,
    critical_window=(0.8, 1.2),
    num_realizations=50
)

# Plot results
fig = plot_phase_transition(results)
```

### Finite Size Analysis
```python
from src.phase_transition import finite_size_analysis, plot_finite_size_effects
import numpy as np

k_values = np.linspace(0.5, 1.5, 30)
N_values = [100, 1000, 10000]

results = finite_size_analysis(k_values, N_values, num_realizations=50)
fig = plot_finite_size_effects(k_values, results)
```

### Jupyter Notebook
```bash
jupyter notebook notebooks/question3_analysis.ipynb
```

## Results - Question 3

### Key Findings

| Aspect | Observation | Theoretical Prediction |
|--------|-------------|----------------------|
| Critical Point | `<k> ≈ 1.0` | `<k>_c = 1` |
| Order Parameter | Continuous transition | S ~ (k - k_c)^β |
| Cluster Size | Peaks at criticality | `<s>` diverges at k_c |
| Finite Size | Sharper for larger N | Sharp only at N → ∞ |

### Physical Interpretation

1. **Phase Transition**: The network undergoes a second-order phase transition at `<k> = 1`
   - Below: Fragmented (subcritical)
   - At: Critical fluctuations, all cluster sizes present
   - Above: Connected (supercritical) with giant component

2. **Divergence**: Average cluster size `<s>` diverges at the critical point in the thermodynamic limit (N → ∞), indicating critical fluctuations

3. **Universality**: This behavior is universal for random networks and analogous to percolation transitions in statistical physics

4. **Real-world Applications**: 
   - Epidemic spreading (critical vaccination threshold)
   - Network robustness (minimum connectivity for communication)
   - Social network formation (critical density for global connectivity)

## AI Usage

This project was developed with assistance from Claude AI (Anthropic) for:
- Understanding NetworkX API and best practices
- Implementing efficient sampling strategy for large graphs
- Debugging path length calculation edge cases

The core algorithms and analysis were implemented based on theoretical understanding of network science and graph theory from course lectures and materials.

## Contributors

[Erfan Shahabi]

## License

This project is for educational purposes as part of Social Networks course, Fall 2025.