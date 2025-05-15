from ctypes import c_int16

import pandas as pd
import matplotlib.pyplot as plt


l_1 = ['Hokej', 'Piłka nożna', 'Koszykówka', 'Tenis', 'Siatkówka']
s_1 = [10.0, 40.0, 20.0, 15.0, 15.0]
c_1 = ['purple', 'lightcoral', 'skyblue', 'green', 'orange']
ex_1 = (0, 0.1, 0, 0, 0)
plt.pie(s_1,labels = l_1,  colors = c_1, explode = ex_1, shadow = True, autopct = '%1.1f%%')
plt.title("Popularność dtscyplin sportowych")

l_2 = ['Golf', 'Lekkoatletyka', 'Pływanie', 'Boks', 'Gimnastyka', 'Kolarstwo']
s_2 = [10.0, 25.0, 20.0, 18.0, 15.0, 12.0]
c_2 = ['lightgrey', 'skyblue', 'lightgreen', 'lightsalmon', 'pink']
ex_2 = (0, 0.1, 0, 0, 0)
plt.title("Popularność dtscyplin sportowych")

plt.pie(s_2, labels= l_2,  colors = c_2, explode = ex_2, shadow = True, autopct = '%1.1f%%')
plt.figure(figsize =(8, 6))

plt.show()