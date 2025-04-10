import pandas as pd
# Utwórz ramkę danych z wynikami pomiarów
pomiary = pd.DataFrame({
'Próbka': ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'],
'Wynik1': [45, 47, 49, 51, 46, 48, 50, 52],
'Wynik2': [120, 150, 110, 190, 200, 115, 140, 180]
})

print(pomiary)

rozstep = pomiary['Wynik1'].max() - pomiary['Wynik1'].min()
print(f"Rozstep: {rozstep}")

odchylenie = pomiary['Wynik1'].std()
print(f"Odchylenie:{odchylenie}")

wariancja = pomiary['Wynik1'].var()
print(f"Wariancja: {wariancja}")

srednia= pomiary['Wynik1'].var()
print(f"mean: {srednia}")

