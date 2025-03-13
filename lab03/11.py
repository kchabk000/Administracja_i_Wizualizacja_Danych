import numpy as np
# 11. Dla tablicy X = np.array([[2, 5, 8], [1, 3, 7], [4, 6, 9]]) oraz tablicy
# Y = np.array([1, 2, 3]), znajdź maksimum pomiędzy każdym elementem X i
# odpowiadającym elementem Y (zastosuj broadcasting)
X = np.array([[2, 5, 8], [1, 3, 7], [4, 6, 9]])
Y = np.array([1, 2, 3])
wynik = np.maximum(X, Y)
print(wynik)