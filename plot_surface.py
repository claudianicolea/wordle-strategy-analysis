import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from simulate_wordle import run_simulations

# PARAMETERS
num_games = 100
w_step = 0.1
save_file = "simulation_results.npy"

w1_values = np.arange(0, 1.0 + w_step, w_step)
w2_values = np.arange(0, 1.0 + w_step, w_step)

W1, W2 = np.meshgrid(w1_values, w2_values)
E = np.zeros_like(W1)

# RUN SIMULATIONS
print("\n--- RUNNING SIMULATIONS ---\n")

for i, w1 in enumerate(w1_values):
    print(f"\n=== w1 = {w1:.2f} ===")
    
    for j, w2 in enumerate(w2_values):
        avg = run_simulations(num_games, w1, w2)
        E[j, i] = avg
    
    print("-" * 30)

# Save results
np.save(save_file, E)
print(f"\nSimulation results saved to {save_file}")

# FIND OPTIMUM
min_idx = np.unravel_index(np.argmin(E), E.shape)
opt_i, opt_j = min_idx[1], min_idx[0]

opt_w1 = w1_values[opt_i]
opt_w2 = w2_values[opt_j]
min_E = E[min_idx]

print("\n--- OPTIMAL STRATEGY ---")
print(f"w1 = {opt_w1:.3f}")
print(f"w2 = {opt_w2:.3f}")
print(f"Minimum average guesses = {min_E:.3f}")

# DERIVATIVES (FINITE DIFFERENCE)
def partial_derivatives(E, i, j, step):
    # central difference if possible
    if 0 < i < E.shape[1] - 1:
        dE_dw1 = (E[j, i+1] - E[j, i-1]) / (2 * step)
    else:
        dE_dw1 = np.nan

    if 0 < j < E.shape[0] - 1:
        dE_dw2 = (E[j+1, i] - E[j-1, i]) / (2 * step)
    else:
        dE_dw2 = np.nan

    return dE_dw1, dE_dw2

dE_dw1, dE_dw2 = partial_derivatives(E, opt_i, opt_j, w_step)

print("\n--- PARTIAL DERIVATIVES AT OPTIMUM ---")
print(f"dE/dw1 ≈ {dE_dw1:.4f}")
print(f"dE/dw2 ≈ {dE_dw2:.4f}")

# PLOT SURFACE
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(W1, W2, E, edgecolor='k', alpha=0.8)

ax.set_xlabel('Frequency weight (w1)')
ax.set_ylabel('Position weight (w2)')
ax.set_zlabel('Average number of guesses')
ax.set_title('Wordle Strategy Optimization Surface')

fig.colorbar(surf, shrink=0.5, aspect=5)

# highlight minimum
ax.scatter(opt_w1, opt_w2, min_E, s=50)
ax.text(opt_w1, opt_w2, min_E + 0.1, f"Min: {min_E:.2f}")

plt.show()