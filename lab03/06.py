import numpy as np
#  Mając tablicę A = np.array([[1, 2, 3], [4, 5, 6]]) oraz tablicę B = np.array([10,
# 20]), wykonaj mnożenie, gdzie każdy wiersz tablicy A jest pomnożony przez odpowiedni
# element tablicy B.
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([10, 20])
wynik = A.T * B
print(wynik.T)