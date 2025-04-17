import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.arange (-3, 1 , 0.1)

y1 = -x ** 2 + 4
y2 = np.exp(x) + 4
y3 = 2*np.cos(3*x)
plt.plot(x, y1, "yellow", linestyle='--', label="$y-x^{2} + 4$")
plt.plot(x, y2, "green", linestyle=':', label="$y=e^{x} + 4$")
plt.plot(x, y3, "pink", linestyle='-', label="$y=2cos(3x)$")
plt.legend()
plt.title("Wykres drugi")
plt.grid(True)
plt.show()

