import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.arange (-3, 1 , 0.1)
y1 = np.exp(4 *x)
y2 = 2*np.cos(3*x)
y3 = x ** 2 + 4
plt.plot( x, y1, "red", linestyle='dotted', label='linear')
plt.plot(x, y2, "blue",linestyle='solid', label = "cos")
plt.plot(x, y3, "green",linestyle='dashed', label = "")
plt.legend()
plt.title("Wykres trzech funkjci")
plt.grid(True)
plt.show()