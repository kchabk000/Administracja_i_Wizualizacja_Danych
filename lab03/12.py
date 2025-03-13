import numpy as np
# 12. Mając tablicę values = np.array([-3, -2, -1, 0, 1, 2, 3]), użyj funkcji uniwersalnej do znalezienia wartości bezwzględnej każdego elementu
values = np.array([-3, -2, -1, 0, 1, 2, 3])
wynik = []
for value in values:
    if value < 0:
        wynik.append(-value)
    else:
        wynik.append(value)
wynik = np.array(wynik)
print(wynik)