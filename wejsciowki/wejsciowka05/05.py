import pandas as pd

series1 = pd.Series([12, 25, 38, 49, 63, 76])
tab1 = series1.to_numpy()
print(tab1.dtype)
print(series1[series1 > 45])