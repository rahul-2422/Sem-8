import numpy as np
import matplotlib.pyplot as plt

# Define the 10 pre-defined situations
situations = [
    (0.2, 0.5),  # Situation 1: λ = 0.2, μ = 0.5
    (0.4, 0.8),  # Situation 2: λ = 0.4, μ = 0.8
    (0.6, 1.0),  # Situation 3: λ = 0.6, μ = 1.0
    (0.8, 1.2),  # Situation 4: λ = 0.8, μ = 1.2
    (0.1, 0.6),  # Situation 5: λ = 0.1, μ = 0.6
    (0.3, 0.9),  # Situation 6: λ = 0.3, μ = 0.9
    (0.5, 1.1),  # Situation 7: λ = 0.5, μ = 1.1
    (0.7, 1.3),  # Situation 8: λ = 0.7, μ = 1.3
    (0.2, 0.7),  # Situation 9: λ = 0.2, μ = 0.7
    (0.4, 1.0)   # Situation 10: λ = 0.4, μ = 1.0
]

# Calculate the mean queue lengths for M/M/1 and M/D/1 systems
mm1_queue_lengths = []
md1_queue_lengths = []

for lam, mu in situations:
    # M/M/1 queue length
    mm1_queue_length = lam / (mu - lam)
    mm1_queue_lengths.append(mm1_queue_length)

    # M/D/1 queue length
    md1_queue_length = (lam / (mu - lam)) * (1 + (lam / (2 * mu)))
    md1_queue_lengths.append(md1_queue_length)

# Plot the results
fig, ax = plt.subplots(figsize=(12, 8))
x = np.arange(len(situations))
ax.plot(x, mm1_queue_lengths, 'x-', label='M/M/1')
ax.plot(x, md1_queue_lengths, 'o-', label='M/D/1')
ax.set_xticks(x)
ax.set_xticklabels([f"Situation {i+1}" for i in range(len(situations))])
ax.set_xlabel('Situation')
ax.set_ylabel('Mean Queue Length')
ax.set_title('Mean Queue Length Comparison: M/M/1 vs M/D/1')
ax.legend()
plt.show()
