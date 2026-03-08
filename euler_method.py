import numpy as np
import matplotlib.pyplot as plt

def dy_dx(y, k, alpha):
    return -k * y**alpha

def euler_method(y0, k, alpha, dx, steps):
    y = np.zeros(steps+1)
    x = np.zeros(steps+1)
    y[0] = y0
    for i in range(steps):
        y[i+1] = y[i] + dx * dy_dx(y[i], k, alpha)
        x[i+1] = x[i] + dx
    return x, y

if __name__ == "__main__":
    x, y = euler_method(1.0, 0.6, 1.2, 0.01, 200)
    plt.plot(x, y)
    plt.xlabel("Guess steps (continuous)")
    plt.ylabel("Fraction of solution space remaining")
    plt.title("Euler Method Approximation of Solution Space Reduction")
    plt.show()