import numpy as np
# 4. Mając tablicę dwuwymiarową M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# oraz jednowymiarową tablicę v = np.array([10, 20, 30]), dodaj v do każdego wiersza M.
M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
v = np.array([10, 20, 30])
wynik = M + v
print(wynik)