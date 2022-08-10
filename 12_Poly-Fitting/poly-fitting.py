# Computational Linear Algebra Ep#12 Polynomial-Fitting
# By: Nick Space Cowboy

import numpy as np
import matplotlib.pyplot as plt
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
    dcnt = 0
    fig.suptitle(title)
    colors = ["orangered", "aqua", "gold", "fuchsia", "lime", "ivory"]
    dummy = np.arange(0, din["Total Numbers"].iloc[-1])
    poly = 0
    for i in range(0, len(line_params[0])):
        poly += line_params[0][i] * (dummy ** i)
    ax.plot(dummy, poly, label="Fitting", color=colors[dcnt + 1], zorder=2, linewidth=2.0)
    ax.plot(din["Total Numbers"], din["Runtime"], label="Runtime Data", color=colors[dcnt], zorder=1)
    dcnt += 1
    plt.legend()
    # plt.show()
    plt.savefig(f"{filename}.jpg", format="jpg")
    
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
    
