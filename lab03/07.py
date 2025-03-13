import numpy as np
# 7. Dla tablicy temps = np.array([0, 10, 20, 30, 40]) (temperatury w stopniach Celsjusza), zamień je na stopnie Fahrenheita używając wzoru F = C * 9/5 + 32.
temps = np.array([0, 10, 20, 30, 40])
zmiana = temps * 9/5 + 32.
print(zmiana)