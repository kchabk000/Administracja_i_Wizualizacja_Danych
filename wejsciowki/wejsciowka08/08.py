import matplotlib.pyplot as plt
labels = ['Rozrywka', 'Mieszkanie', 'Transport', 'Jedzenie']
sizes = [14.9, 42.6, 16.0, 26.6]
colors = ['red', 'dodgerblue', 'orange', 'green']

plt.pie(sizes, labels = labels , colors = colors, shadow = True, startangle = 45, autopct ='%1.1f%%')
plt.title('Miesięczne wydatki domowe \n (kwiecień 2025)')
plt.tight_layout()
plt.show()
