import numpy as np
import numpy.char

# 4. Dla tablicy arr = np.array(["python.data.science", "machine.learning"]), użyj
# metody numpy.char.split() z odpowiednim separatorem, aby rozdzielić tekst na części

arr = np.array(["python.data.science", "machine.learning"])
arr1 = np.char.split(arr, ".")
print(arr1)