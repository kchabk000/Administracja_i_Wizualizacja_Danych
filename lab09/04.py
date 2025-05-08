import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

football = pd.read.csv("footfall_shopping_centers.csv", parse_dates = ["date"])
x = football["date"]
y football[:"mall_a"]
plt.scatter(x,y)
plt.xticks(rotation=30)
plt.title("Dane o centrach handlowych")
plt.grid(True, alpha=0.7)
plt.xlabel("Dni")
plt.ylabel("Wartosc")
plt.tight_layout()
plt.savefig("zad4.eps")
plt.show()