import numpy as np
# 2. Dla tablicy arr = np.array(["PYTHON", "NUMPY", "DATA SCIENCE"]), użyj metody
# numpy.strings.lower() aby zamienić wszystkie litery na małe, a następnie metodę
# numpy.strings.title() aby każde słowo zaczynało się wielką literą.

arr = np.array(["PYTHON", "NUMPY", "DATA SCIENCE"])
arr = np.strings.lower(arr)
arr = np.strings.title(arr)
print(arr)