import numpy as np
# 5. Mając tablicę arr = np.array([" python ", " numpy ", " pandas "]),
# użyj metody numpy.strings.strip() aby usunąć białe znaki z początku i końca
# każdego elementu.

arr = np.array([" python ", " numpy ", " pandas "])
arr1 = np.strings.strip(arr," ")
print(arr1)