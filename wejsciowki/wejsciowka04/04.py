import numpy as np
codes = np.array(["PL-Warsaw","UK-London", "US-NewYork"])
A = np.char.split(codes, "-")

print(A)