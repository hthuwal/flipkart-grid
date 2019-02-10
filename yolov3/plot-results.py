import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys

titles = ["xloss", "yloss", "wloss", "hloss", "cnfloss", "clsloss", "lossloss", "maPvalid", "Pvalid", "Rvalid"]

results_file = sys.argv[1]
plot_file = sys.argv[2]

results = np.loadtxt(results_file, dtype=str)
results = np.delete(results, [1, 9, 10, 11, 12, 13, 14, 15], axis=1).astype(float)
epochs = results[:, 0]
results = results[:, 1:]

plt.clf()
my_dpi = 300
plt.figure(figsize=(1920 / my_dpi, (1000 * 5) / my_dpi), dpi=my_dpi)
colors = [cm.jet(x) for x in np.linspace(0.00, 1.00, len(titles))]

for i in range(len(titles)):
    plt.subplot(5, 2, i + 1)
    plt.plot(epochs, results[:, i], color=colors[i], label=titles[i])
    plt.legend()

plt.savefig(plot_file, dpi=my_dpi)
