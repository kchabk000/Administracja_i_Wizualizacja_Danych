import numpy as np
# 10. Utwórz dwie tablice: A = np.array([[1, 2], [3, 4]]) oraz B = np.array([5, 6]),
# a następnie wykonaj operację dzielenia modulo (%) każdego wiersza A przez tablicę B.
A = np.array([[1, 2], [3, 4]])
B = np.array([5, 6])
wynik = A % B
print(wynik)
