import numpy as np
# 6. Dla dwóch wektorów a = np.array([2, 4, 6]) i b = np.array([1, 3, 5]), oblicz
# ich iloczyn skalarny używając funkcji np.dot(), a następnie za pomocą operatora @.
a = np.array([2, 4, 6])
b = np.array([1, 3, 5])
c = np.dot(a, b)
d = a @ b
print(c)
print(d)
    