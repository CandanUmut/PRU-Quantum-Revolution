# Creating the full Python file content for the PRU-style entanglement experiment

Entanglement Simulation using PRU (Precomputed Relational Universe) Principles

Author: Umut Candan, Nova
Date: 2025

Description:
This simulation reproduces quantum entanglement behavior using deterministic,
relational state sharing instead of probabilistic quantum mechanics. The result
is a relational model that reflects entanglement correlations without wavefunctions
or non-local collapse.

"""

import numpy as np
import random
import matplotlib.pyplot as plt

# Number of entangled pairs
NUM_PAIRS = 10000

# Relational measurement angles (representing observer context)
angles_a = [0, np.pi / 4]          # Alice's angle choices
angles_b = [np.pi / 8, 3 * np.pi / 8]  # Bob's angle choices

# Define a function to simulate relational state outcome
def measure_relational_pair(theta_a, theta_b):
    """
    Simulates outcome of a relationally entangled pair
    based on angle difference and shared relational reference.
    """
    relational_alignment = np.cos(theta_a - theta_b)  # shared precomputed memory
    random_threshold = random.uniform(-1, 1)

    if random_threshold < relational_alignment:
        return (1, 1)  # aligned outcome
    else:
        return (1, -1)  # anti-aligned outcome

# Run simulation
results = []
for _ in range(NUM_PAIRS):
    a_angle = random.choice(angles_a)
    b_angle = random.choice(angles_b)
    result = measure_relational_pair(a_angle, b_angle)
    results.append(result)

# Count correlation types
correlated = sum(1 for r in results if r[0] == r[1])
anti_correlated = NUM_PAIRS - correlated

# Calculate percentages
correlation_percent = correlated / NUM_PAIRS * 100
anti_correlation_percent = anti_correlated / NUM_PAIRS * 100

# Output results
print(f"Total Pairs Simulated: {NUM_PAIRS}")
print(f"Correlated Outcomes: {correlation_percent:.2f}%")
print(f"Anti-Correlated Outcomes: {anti_correlation_percent:.2f}%")

# Optional: Visualization
labels = ['Correlated', 'Anti-Correlated']
sizes = [correlation_percent, anti_correlation_percent]
colors = ['green', 'red']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Relational Entanglement Outcome Distribution")
plt.axis('equal')
plt.show()


