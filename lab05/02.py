import pandas as pd
slownik = {'jabłka': 120, 'gruszki': 85, 'śliwki':95, 'banany': 140}
series2 = pd.Series(slownik)

series2.name = "Owoce"
series2.index.name = "Produkt"

