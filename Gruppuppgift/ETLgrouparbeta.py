import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

file_path = 'processed_data_befolkningsförändringar.csv'  
data = pd.read_csv(file_path)

data['procentuell_ökning'] = data['folkmängd'].pct_change() * 100

data.sort_values(by='år', ascending=True, inplace=True)

#print(data)

""" 


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
plt.show()

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

plt.show()

"""
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





#totalt antal födda och döda och inflyttningar och utflyttningar

# Beräkna nettoförändringen av befolkningen per år
data['nettoförändring'] = data['födda'] - data['döda'] + data['samtliga inflyttningar'] - data['samtliga utflyttningar']

# Skapa en linjegraf
plt.figure(figsize=(12, 6))
plt.plot(data['år'], data['nettoförändring'], marker='o', linestyle='-', color='blue', label='Nettoförändring')

# Anpassa diagrammet
plt.title('Nettoförändring av befolkningen per år')
plt.xlabel('År')
plt.ylabel('Antal personer')
plt.axhline(0, color='red', linestyle='--', linewidth=0.8, label='Ingen förändring')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.xticks(data['år'])

# Visa diagrammet
plt.tight_layout()

plt.show()


data['nettoförändring'] = data['födda'] - data['döda'] + data['samtliga inflyttningar'] - data['samtliga utflyttningar']

# Skapa områdesdiagram
plt.figure(figsize=(12, 6))
plt.fill_between(data['år'], data['nettoförändring'], where=(data['nettoförändring'] >= 0), 
                color='green', alpha=0.6, label='Befolkningsökning')
plt.fill_between(data['år'], data['nettoförändring'], where=(data['nettoförändring'] < 0), 
                color='red', alpha=0.6, label='Befolkningsminskning')

# Anpassa diagrammet
plt.title('Områdesdiagram: Nettoförändring av befolkningen per år')
plt.xlabel('År')
plt.ylabel('Förändring i antal personer')
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend()

# Visa diagrammet
plt.tight_layout()
plt.show()


# Rensa och förbered data
data['år'] = pd.to_numeric(data['år'], errors='coerce')
data['nettoförändring'] = data['födda'] - data['döda'] + data['samtliga inflyttningar'] - data['samtliga utflyttningar']
data = data.dropna()

# Träna en linjär regressionsmodell
X = data['år'].values.reshape(-1, 1)
y = data['nettoförändring'].values
model = LinearRegression()
model.fit(X, y)

# Gör förutsägelser för de kommande 10 åren
future_years = np.arange(data['år'].max() + 1, data['år'].max() + 11).reshape(-1, 1)
future_predictions = model.predict(future_years)

# Rita historiska data och framtida förutsägelser
plt.figure(figsize=(12, 6))
plt.fill_between(data['år'], data['nettoförändring'], where=(data['nettoförändring'] >= 0), 
                color='green', alpha=0.6, label='Befolkningsökning (Historisk)')
plt.fill_between(data['år'], data['nettoförändring'], where=(data['nettoförändring'] < 0), 
                color='red', alpha=0.6, label='Befolkningsminskning (Historisk)')
plt.plot(future_years, future_predictions, linestyle='--', marker='o', color='orange', label='Prognos (Framtid)')

# Anpassa diagrammet
plt.title('Nettoförändring av befolkningen per år (Historisk & Prognos)')
plt.xlabel('År')
plt.ylabel('Förändring i antal personer')
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend()

# Visa diagrammet
plt.tight_layout()
plt.show()


"""
"""

# Förbered data
data['år'] = pd.to_numeric(data['år'], errors='coerce')
data['nettoförändring'] = data['födda'] - data['döda'] + data['samtliga inflyttningar'] - data['samtliga utflyttningar']
data = data.dropna()

# Träna en linjär regressionsmodell
X = data['år'].values.reshape(-1, 1)
y = data['nettoförändring'].values
model = LinearRegression()
model.fit(X, y)

# Förutsägelser för framtiden
last_year = data['år'].max()
future_years = np.arange(last_year, last_year + 20).reshape(-1, 1)  # Prognosen börjar direkt
future_predictions = model.predict(future_years)

# Skapa figuren
plt.figure(figsize=(12, 6))

# Historiska data
plt.fill_between(data['år'], data['nettoförändring'], where=(data['nettoförändring'] >= 0), 
                color='green', alpha=0.6, label='Befolkningsökning')
plt.fill_between(data['år'], data['nettoförändring'], where=(data['nettoförändring'] < 0), 
                color='red', alpha=0.6, label='Befolkningsminskning')

# Prognoslinje (kopplar direkt från historik)
plt.plot(np.concatenate([data['år'].values[-1:], future_years.flatten()]), 
        np.concatenate([data['nettoförändring'].values[-1:], future_predictions]), 
        linestyle='--', marker='o', color='blue', label='Prognos (Framtid)')

# Prognosområde (olika färger beroende på om värdet är över eller under 0)
plt.fill_between(future_years.flatten(), future_predictions, where=(future_predictions >= 0), 
                color='blue', alpha=0.2, label="Prognos Ökning")
plt.fill_between(future_years.flatten(), future_predictions, where=(future_predictions < 0), 
                color='red', alpha=0.4, label="Prognos Minskning")

# Justera layout
plt.title('Nettoförändring av befolkningen per år (Historisk & Prognos utan lucka)')
plt.xlabel('År')
plt.ylabel('Förändring i antal personer')
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend()

# Visa diagrammet
plt.tight_layout()
plt.show()



"""


"""






# Förbered data
data['år'] = pd.to_numeric(data['år'], errors='coerce')
data['nettoförändring'] = data['födda'] - data['döda'] + data['samtliga inflyttningar'] - data['samtliga utflyttningar']
data = data.dropna()

# Träna en linjär regressionsmodell
X = data['år'].values.reshape(-1, 1)
y = data['nettoförändring'].values
model = LinearRegression()
model.fit(X, y)

# Förutsägelser för framtiden
last_year = data['år'].max()
future_years = np.arange(last_year, last_year + 20).reshape(-1, 1)  # Prognosen börjar direkt
future_predictions = model.predict(future_years)

# Skapa figuren
plt.figure(figsize=(12, 6))

# Historiska data
plt.fill_between(data['år'], data['nettoförändring'], where=(data['nettoförändring'] >= 0), 
                color='green', alpha=0.6, label='Befolkningsökning')
plt.fill_between(data['år'], data['nettoförändring'], where=(data['nettoförändring'] < 0), 
                color='red', alpha=0.6, label='Befolkningsminskning')

# Prognoslinje (kopplar direkt från historik)
plt.plot(np.concatenate([data['år'].values[-1:], future_years.flatten()]), 
        np.concatenate([data['nettoförändring'].values[-1:], future_predictions]), 
        linestyle='--', marker='o', color='blue', label='Prognos (Framtid)')

# Prognosområde (olika färger beroende på om värdet är över eller under 0)
plt.fill_between(future_years.flatten(), future_predictions, where=(future_predictions >= 0), 
                color='blue', alpha=0.2, label="Prognos Ökning")
plt.fill_between(future_years.flatten(), future_predictions, where=(future_predictions < 0), 
                color='purple', alpha=0.4, label="Prognos Minskning")

# Skapa en sammanfattningslista av viktiga tal
summary_text = f"""
        Summa historiska födda: {data['födda'].sum()}
        Summa historiska döda: {data['döda'].sum()}
        Summa inflyttningar: {data['samtliga inflyttningar'].sum()}
        Summa utflyttningar: {data['samtliga utflyttningar'].sum()}
        Total nettoförändring: {data['nettoförändring'].sum()}
        Prognos 20 år framåt: {int(future_predictions.sum())}
"""

# Placera sammanfattningsrutan i grafen
plt.gca().text(0.02, 0.98, summary_text, transform=plt.gca().transAxes, fontsize=10,
        verticalalignment='top', bbox=dict(boxstyle="round,pad=0.5", facecolor="white", alpha=0.8))

# Justera layout
plt.title('Nettoförändring av befolkningen per år (Historisk & Prognos utan lucka)')
plt.xlabel('År')
plt.ylabel('Förändring i antal personer')
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend()
# Visa diagrammet
plt.tight_layout()
plt.show()




# Konvertera år till numeriskt format
data['år'] = pd.to_numeric(data['år'], errors='coerce')

# Beräkna nettoförändring om den saknas
if 'nettoförändring' not in data.columns:
        data['nettoförändring'] = data['födelseöverskott'] + data['flyttningsöverskott totalt']

# Träna en linjär regressionsmodell för att förutsäga framtida nettoförändring
X = data[['år']].values  # År som input
y = data['nettoförändring'].values  # Nettoförändring som output

model = LinearRegression()
model.fit(X, y)

# Skapa framtida år för prognos (200 år framåt)
future_years = np.arange(data['år'].max() + 1, data['år'].max() + 35) .reshape(-1, 1)
future_predictions = model.predict(future_years)

# Skapa färger för framtida data (grön för positiv, röd för negativ)
colors = ['green' if val > 0 else 'red' for val in future_predictions]

# Skapa diagrammet
plt.figure(figsize=(12, 6))

# Historiska data
plt.bar(data['år'], data['nettoförändring'], color=['green' if val > 0 else 'red' for val in data['nettoförändring']], edgecolor='black', label='Historiska data')

# Prognosdata
plt.bar(future_years.flatten(), future_predictions, color=colors, edgecolor='black', alpha=0.5, label='Prognos (35 år framåt)')

# Anpassa diagrammet
plt.title("📊 Nettoförändring av befolkningen per år (Historik & Prognos 35 år)", fontsize=14)
plt.xlabel("År", fontsize=12)
plt.ylabel("Förändring i antal personer", fontsize=12)
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)  # Linje vid 0
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend()

# Visa diagrammet
plt.tight_layout()
plt.show()