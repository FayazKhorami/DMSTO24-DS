

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {"Category": ["A", "B", "C", "D", "E"], "Sales": [100, 200, 300, 400, 500]}

df = pd.DataFrame(data) 

sns.barplot(x="Category", y="Sales", data=df)  

sns.lineplot(x="Category", y="Sales", data=df)

plt.show()
