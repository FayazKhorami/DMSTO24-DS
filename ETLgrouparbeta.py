import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

file_path = 'processed_data_befolkningsförändringar.csv'  
data = pd.read_csv(file_path)

data['procentuell_ökning'] = data['folkmängd'].pct_change() * 100

data.sort_values(by='år', ascending=True, inplace=True)

print(data)




"""

plt.figure(figsize=(10, 6))
plt.plot(data['år'], data['procentuell_ökning'], marker='o', linestyle='-', label='Procentuell förändring')

plt.title('Procentuell förändring av folkmängden per år')
plt.xlabel('År')
plt.ylabel('Procentuell förändring (%)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(0, color='black', label='Ingen förändring')
plt.legend()
plt.xticks(data['år'])

plt.tight_layout()


"""



"""


plt.figure(figsize=(10, 6))
plt.fill_between(data['år'], data['procentuell_ökning'], color='skyblue', alpha=0.5, label='Procentuell förändring')
plt.plot(data['år'], data['procentuell_ökning'], color='blue', linewidth=2, label='Trendlinje')

plt.title('Procentuell förändring av folkmängden per år')
plt.xlabel('År')
plt.ylabel('Procentuell förändring (%)')
plt.grid(True, linestyle='--', alpha=0.9)
plt.axhline(0, color='red', linestyle='--', linewidth=0.9, label='Ingen förändring')
plt.legend()
plt.xticks(data['år'])

plt.tight_layout()




"""


# Förbered data
X = data['år'].values.reshape(-1, 1)  # År som input
y = data['tillväxttakt'].values          # Folkmängd som output

# Träna en enkel linjär regressionsmodell
model = LinearRegression()
model.fit(X, y)

# Gör förutsägelser för de kommande 10 åren
future_years = np.arange(data['år'].max() + 1, data['år'].max() + 11).reshape(-1, 1)
future_predictions = model.predict(future_years)

# Rita resultaten
plt.figure(figsize=(10, 6))
plt.scatter(data['år'], data['tillväxttakt'], color='blue', label='Historiska data')
plt.plot(np.vstack((X, future_years)), 
        np.concatenate((model.predict(X), future_predictions)), 
        color='red', label='Modellens förutsägelse')

# Anpassa diagrammet
plt.title('Förutsägelse av tillväxttakt (10 år framåt)')
plt.xlabel('År')
plt.ylabel('tillväxttakt')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Visa diagrammet
plt.tight_layout()
plt.show()

