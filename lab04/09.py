import numpy as np
# 9. Dla macierzy M = np.array([[6, 2], [3, 9]]), oblicz jej wyznacznik używając funkcji np.linalg.det() oraz znajdź macierz odwrotną za pomocą funkcji
# np.linalg.inv(). Sprawdź czy iloczyn macierzy M i jej odwrotności daje macierz
# jednostkową
M = np.array([[6, 2], [3, 9]])
wyznacznik = np.linalg.det(M)
odwrotna = np.linalg.inv(M)
iloczyn = M @ odwrotna
print(wyznacznik)
print(odwrotna)
print(iloczyn)