import numpy as np
#Utwórz tablicę 5×5 wypełnioną liczbami od 1 do 25 i znajdź wartość maksymalną oraz minimalną.

x = np.arange(1,26).reshape((5,5))
print(x.min())
print(x.max())

