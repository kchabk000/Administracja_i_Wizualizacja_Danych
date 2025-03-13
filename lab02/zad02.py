import numpy as np

# 2. Stwórz macierz 4×4 wypełnioną liczbami od 1 do 16 i wyświetl jej wymiar oraz kształt.

macierz = np.arange(1,17)
a = macierz.reshape(4,4)
print("macierz 4x4: \n", a)
print("wymiar: ", a.ndim)
print("ksztalt: ", a.shape)
