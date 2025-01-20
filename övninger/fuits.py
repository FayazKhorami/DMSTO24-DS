

import pandas as pd
import matplotlib.pyplot as plt


DF = pd.read_csv("fruits.csv")

GroupInformation = DF.groupby("Product").sum("Sales")

print(GroupInformation)

plt.bar(GroupInformation.index, GroupInformation["Sales"])

plt.title("Total försäljning per produkt")

plt.xlabel("Produkt")

plt.ylabel("Försäljning")

plt.show()

timeTid = DF.groupby("Date").sum("Sales")

plt.plot(timeTid.index, timeTid["Sales"])

plt.title("Försäljning över tid")

plt.xlabel("Datum")

plt.ylabel("Försäljning")


# gör att namnet på datumet inte överlappar
plt.xticks(rotation=45)

plt.show()
