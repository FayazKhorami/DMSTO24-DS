
"""

import matplotlib.pyplot as plt
import numpy as np
import math

x_vals = np.linspace(0, 20, 20)
print(x_vals)
y_vals = [math.sqrt(i) for i in x_vals]
plt.plot(x_vals, y_vals)

plt.title("Square root of x")
plt.ylabel("Viktoria ser ut som tant")
plt.xlabel("för varje dag som går")
plt.grid(True)


plt.show()




import matplotlib.pyplot as plt


kurs = [
    "Datamodellering och design",
    "Att arbeta i projekt",
    "Data-arkitektur",
    "Data Science",
    "Databastyper",
    "Statistik och dataanalys",
    "Datakvalitet",
    "Metadata och webbanalys",
    "Datasäkerhet",
    "Datastyrning",
    "Examensarbete",
    "LIA"
]

längd = [30, 20, 25, 40, 25, 35, 25, 30, 20, 30, 20, 100]


plt.figure(figsize=(12, 8))
plt.barh(kurs, längd, color="skyblue")  

plt.xlabel("Vikt", fontsize=12)
plt.ylabel("Kurser", fontsize=12)
plt.title("Fördelning av kurser och LIA", fontsize=16)
plt.grid(axis="x", linestyle="dashdot", alpha=0.9)


plt.tight_layout()


plt.show()




import matplotlib.pyplot as plt

labels = "Datamodellering och design", "Att arbeta i projekt", "Data-arkitektur", "Data Science", "Databastyper", "Statistik och dataanalys", "Datakvalitet", "Metadata och webbanalys", "Datasäkerhet", "Datastyrning", "Examensarbete", "LIA"

values = [   30,   20,   25,   40,   25,   35,   25,   30,   20,  30,   20,  100]

explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1) 

plt.pie(values, explode=explode, labels=labels, autopct='%3.3f%%', shadow=True)

plt.axis("equal")

plt.show()

"""


