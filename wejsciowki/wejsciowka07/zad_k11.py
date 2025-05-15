import pandas as pd
import matplotlib.pyplot as plt

gwiazdy_x = [13, 28, 28, 29, 32, 37]
gwiazdy_y = [20, 34, 32, 5, 2, 21]

trojkat_x = [12, 28, 28, 29, 33, 36]
trojkat_y = [ 55, 22, 28, 55, 32,42]

plt.figure(figsize = (8, 6))
plt.scatter(gwiazdy_x, gwiazdy_y, color = 'brown', marker = '*', label = 'gwiazdy', s = 100)
plt.scatter(trojkat_x, trojkat_y, color = 'green', marker = 'v', label = 'trojkat', s = 100)

plt.title('Wykres punktowy - 2 x 6 punktów')
plt.legend()
plt.grid(True)
plt.show()