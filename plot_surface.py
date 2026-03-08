import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from simulate_wordle import run_simulations

num_games = 10  # number of games per w1/w2 combination
w_step = 0.1     # grid step for weights (smaller steps -> smoother but more computation)
save_file = "simulation_results.npy"

w1_values = np.arange(0, 1.0 + w_step, w_step)  # frequency weight
w2_values = np.arange(0, 1.0 + w_step, w_step)  # position weight
W1, W2 = np.meshgrid(w1_values, w2_values)

E = np.zeros_like(W1)

for i in range(len(w1_values)):
    for j in range(len(w2_values)):
        if (j * len(w1_values) + i) % 10 == 0:
            print(f"Simulating w1 = {w1_values[i] : .2f}, w2 = {w2_values[j] : .2f}")
        E[j, i] = run_simulations(num_games, w1_values[i], w2_values[j])
np.save(save_file, E)
print(f"Simulation results saved to {save_file}")

# find optimal strategy
min_idx = np.unravel_index(np.argmin(E), E.shape)
opt_w1 = W1[min_idx]
opt_w2 = W2[min_idx]
min_E = E[min_idx]

print(f"Optimal strategy: w1 = {opt_w1 : .2f}, w2 = {opt_w2 : .2f}, Avg guesses = {min_E : .2f}")

# plot 3d surface
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection = '3d')
surf = ax.plot_surface(W1, W2, E, cmap = 'viridis', edgecolor = 'k', alpha = 0.8)

ax.set_xlabel('Frequency weight (w1)')
ax.set_ylabel('Position weight (w2)')
ax.set_zlabel('Average bumber of guesses')
ax.set_title('Wordle strategy optimization surface')

fig.colorbar(surf, shrink = 0.5, aspect = 5)

ax.scatter(opt_w1, opt_w2, min_E, color = 'red', s = 50)
ax.text(opt_w1, opt_w2, min_E + 0.1, f"Min: {min_E : .2f}", color = 'red')

plt.show()