import numpy as np
import matplotlib.pyplot as plt

situations = [
  (0.2, 0.5),
  (0.4, 0.8),
  (0.6, 1.0),
  (0.8, 1.2),
  (0.1, 0.6),
  (0.3, 0.9),
  (0.5, 1.1),
  (0.7, 1.3),
  (0.2, 0.7),
  (0.4, 1.0) 
]

mm1_queue_lengths = []
md1_queue_lengths = []

for lmd, mu in situations:
  rho = lmd/mu

  # M/M/1 queue length
  mm1_queue_length = (rho*rho) / (1-rho)
  mm1_queue_lengths.append(mm1_queue_length)

  # M/D/1 queue length (assuming Constant service time distribution)
  md1_queue_length = (rho*rho) / (2*(1-rho))
  md1_queue_lengths.append(md1_queue_length)

fig, ax = plt.subplots(figsize=(12, 8))
x = np.arange(len(situations))
ax.plot(x, mm1_queue_lengths, '-o', color='green', label='M/M/1')
ax.plot(x, md1_queue_lengths, '-o', color='blue', label='M/D/1')
ax.set_xticks(x)
# ax.set_xticklabels([f"λ={lmd}\nμ={mu}" for lmd, mu in situations])
ax.set_xticklabels([f"ρ={(lmd/mu):.1f}" for lmd, mu in situations])
ax.set_xlabel('Situation')
ax.set_ylabel('Mean Queue Length')
ax.set_title('Mean Queue Length Comparison: M/M/1 vs M/D/1')
ax.legend()
plt.show()