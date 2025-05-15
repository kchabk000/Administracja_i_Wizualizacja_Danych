import pandas as pd
import matplotlib.pyplot as plt

labels = ['Odzieżowe', 'Spożywcze', 'Meblowe', 'Inne']
sizes = [24.8, 13.0, 6.7, 55.5]
colors = ['lightcoral', 'skyblue', 'lightgreen', 'lightgrey']
explode = (0.1, 0, 0, 0)

plt.figure(figsize =(8, 6))
plt.pie(sizes, labels = labels, colors = colors, startangle = 25, explode = explode, shadow = True, autopct=  '%1.1f%%')
plt.title('Wyniki sprzedaży - II-IV 2017')
plt.axis('equal')
plt.show()