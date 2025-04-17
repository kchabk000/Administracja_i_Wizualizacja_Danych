import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 3. W jednym pliku wykonaj poniższe czynności:
# • załaduj dane z pliku cena_paliwa11.xlsx jako ramkę danych (Data Frame),
# • wybierz dane dotyczące Benzyny 95,
# • stwórz wykres liniowy na podstawie danych z powyższego podpunktu, każdy rok to
# inna linia, style, kolory i szerokości linii muszą być inne niż standardowe, oś pozioma -
# miesiące,
# • dodaj na wykres siatkę (poziome i pionowe linie).
# • dodaj legendę w lewym dolnym rogu.
# • zapisz wykres w formacie png za pomocą kodu.

dane =pd.read_excel("cena_paliwa11.xlsx")