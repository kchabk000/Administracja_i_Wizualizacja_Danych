import pandas as pd
dane = pd.read_csv('travel23.csv', sep = ';', header = 'infer')
print(dane.head())
print(dane.dtypes)
Kolumny = ['Transport', 'Zakwaterowanie', 'Jedzenie', 'Zwiedzanie', 'Inne']
dane[Kolumny] = dane[Kolumny].astype(float)