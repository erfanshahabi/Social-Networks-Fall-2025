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
git clone <your-repo-url>
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
│   ├── networks.py          # Network creation functions
│   ├── analysis.py          # Analysis and simulation
│   └── visualization.py     # Plotting functions
├── tests/
│   ├── test_networks.py     # Network tests
│   └── test_analysis.py     # Analysis tests
├── notebooks/
│   └── question1_analysis.ipynb  # Main analysis notebook
└── results/
    └── plots/               # Output plots
```

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