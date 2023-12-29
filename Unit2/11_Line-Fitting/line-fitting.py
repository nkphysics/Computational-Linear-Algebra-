# Computational Linear Algebra Ep#11 Line-Fitting
# By: Nick Space Cowboy

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def linefit(x_data, y_data):
	b = np.array(y_data)
	A = np.ones((len(b), 2))
	A[:,1] = np.array(x_data)
	lsq = lsq = np.linalg.lstsq(A, b.T, rcond=None)
	x = lsq[0]
	norm = lsq[1][0]**(0.5)
	return [x, norm]
	
def plot(din, line_params, title, filename):
	plt.style.use("dark_background")
	fig, ax = plt.subplots(sharey=True)
	ax.set_ylabel("Time (s)")
	ax.set_xlabel("# of Random Ints Generated")
	dcnt = 0
	fig.suptitle(title)
	colors = ["orangered", "aqua", "gold", "fuchsia", "lime", "ivory"]
	dummy = np.arange(0, din["Total Numbers"].iloc[-1])
	line = line_params[0][0] + (line_params[0][1] * dummy)
	ax.plot(dummy, line, label="Line Fit", color=colors[dcnt + 1], zorder=2, linewidth=2.0)
	ax.plot(din["Total Numbers"], din["Runtime"], label="Runtime Data", color=colors[dcnt], zorder=1)
	dcnt += 1
	plt.legend()
	plt.savefig(f"{filename}.jpg", format="jpg")
	
if __name__ == "__main__":
	data = pd.read_csv("std-rust_test_100000.0.csv")
	fit = linefit(data["Total Numbers"], data["Runtime"])
	print(f"Slope: {fit[0][1]}")
	print(f"Intercept: {fit[0][0]}")
	print(f"Norm: {fit[1]}")
	plot(data, fit, "Rust Runtime Fit", "rust-runtime-fit")
	
