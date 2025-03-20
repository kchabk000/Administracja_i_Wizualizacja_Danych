import numpy as np
# 3. Połącz dwie tablice arr1 = np.array(["machine", "deep"]) i arr2 = np.array(["learning",
# "networks"]) za pomocą metody numpy.strings.add(), a następnie dodaj między
# nimi spację używając numpy.strings.replace().

arr1 = np.array(["machine", "deep"])
arr2 = np.array(["learning","networks"])
arr3 = np.strings.add(arr1, arr2)
print(arr3)
arr4 = np.strings.replace(arr3, arr1, arr1+" ")
print(arr4)