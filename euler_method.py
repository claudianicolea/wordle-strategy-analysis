import numpy as np
import matplotlib.pyplot as plt

def dx_dt(x, k=0.5, alpha=1.0):
    """Differential equation: rate of reduction of remaining words"""
    return -k * x**alpha

def euler_method(x0=1.0, k=0.5, alpha=1.0, dt=0.01, steps=100):
    """Approximate solution of dx/dt using Euler's method"""
    x = np.zeros(steps+1)
    t = np.zeros(steps+1)
    x[0] = x0
    for i in range(steps):
        x[i+1] = x[i] + dt * dx_dt(x[i], k, alpha)
        t[i+1] = t[i] + dt
    return t, x

if __name__ == "__main__":
    t, x = euler_method(x0=1.0, k=0.6, alpha=1.2, dt=0.01, steps=200)
    plt.plot(t, x)
    plt.xlabel("Guess steps (continuous)")
    plt.ylabel("Fraction of solution space remaining")
    plt.title("Euler Method Approximation of Solution Space Reduction")
    plt.show()