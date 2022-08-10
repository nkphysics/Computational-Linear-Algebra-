# Computational Linear Algebra Ep#11 Line-Fitting
# By: Nick Space Cowboy

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import pandas as pd

def polyfit(x_data, y_data, order):
    aorder = order + 1
    b = np.array(y_data)
    A = np.ones((len(b), aorder))
    for i in range(1, aorder):
        A[:,i] = np.array(x_data) ** i
    lsq = np.linalg.lstsq(A, b.T, rcond=None)
    x = lsq[0]
    try: 
        norm = lsq[1][0]**(0.5)
        return [x, norm]
    except IndexError:
        print("WARNING: Potential Overfit")
        mnorm = sum((np.dot(A, x) - b) ** 2) ** (0.5)
        return [x, mnorm]
    
def plot(din, line_params, title, filename):
    plt.style.use("dark_background")
    fig, ax = plt.subplots(sharey=True)
    ax.set_ylabel("Time (s)")
    ax.set_xlabel("# of Random Ints Generated")
    x = np.arange(0, din["Total Numbers"].iloc[-1], 1e3)
    y = 0
    for i in range(0, len(line_params[0])):
        y += line_params[0][i] * (x ** i)
    poly, = ax.plot([], [], zorder=2, linewidth=2.0, color="aqua", label="Line Fit")
    
    def animate(n, x, y, line):
        poly.set_data(x[:n], y[:n])
        return line,
        
    fig.suptitle(title)
    ax.plot(din["Total Numbers"], din["Runtime"], label="Runtime Data", color="orangered", zorder=1)
    plt.legend()
    ani = animation.FuncAnimation(fig, animate, len(x), fargs=[x, y, poly]) 
    ani.save(f"{filename}.mp4", fps=5)
    
if __name__ == "__main__":
    data = pd.read_csv("std-rust_test_100000.0.csv")
    for i in range(1, 5):
        print(f"{i} order polynomial fit")
        fit = polyfit(data["Total Numbers"], data["Runtime"], i)
        c = 0
        for j in fit[0]:
            print(f"C{c}: {j}")
            c += 1
        print(f"Norm: {fit[1]}")
        print("")
        # plot(data, fit, f"{i}th Order Polyomial Rust Runtime Fit", f"rust-runtime-fit{i}")
    
