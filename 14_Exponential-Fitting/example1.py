# Computational Linear Algebra Ep#14 Exponential-Fitting
# By: Nick Space Cowboy

import numpy as np
import matplotlib.pyplot as plt

def expfit(x_data, y_data):
    b = np.log(y_data)
    A = np.ones((len(b), 2))
    A[:,1] = np.array(x_data)
    lsq = np.linalg.lstsq(A, b.T, rcond=None)
    x = lsq[0]
    x[0] = np.exp(x[0])
    norm = lsq[1][0]**(0.5)
    return [x, norm]
        
def exponent(x, const, alpha):
    return const * np.exp(alpha * x)
    
def plot(data, params, title):
    plt.style.use("dark_background")
    fig, ax = plt.subplots(sharey=True)
    ax.set_ylabel(r"$f(x)$")
    ax.set_xlabel("x-axis")
    fig.suptitle(title)
    x, y = data
    sdomain = np.arange(x[0], x[-1], 0.1)
    sfit = exponent(sdomain, params[0], params[1])
    ax.plot(sdomain, sfit, label="Fit Exponential", color="blue", zorder=0)
    ax.scatter(x, y, color="red", s=10, label="Data", zorder=1)
    plt.legend()
    plt.show()
    
if __name__ == "__main__":
    domain = np.linspace(0, 20, num=20)
    fx = exponent(domain, 3, -0.23)
    fit = expfit(domain, fx)
    c = 0
    for j in fit[0]:
        print(f"C{c}: {j}")
        c += 1
    print(f"Norm: {fit[1]}")
    plot((domain, fx), fit[0], "Exponential Fit")
    
