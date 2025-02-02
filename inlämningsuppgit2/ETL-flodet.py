

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt

# Ändra visningsinställningar för att visa hela datasetet utan punkter
pd.set_option("display.max_columns", None)  # Visa alla kolumner
pd.set_option("display.max_rows", None)  # Visa alla rader
pd.set_option("display.width", None)     # Anpassa bredden dynamiskt

# Här anger jag sökvägen till min CSV-filen
file_path = "inlämningsuppgit2\sjukhus.csv"

# här jag läser in datan från CSV-filen
data = pd.read_csv(file_path, encoding='latin1')


# Tar bort rader som innehåller saknade värden
data = data.dropna()

# Tar bort kolumnerna 'xkoord' och 'ykoord' då jag inte behöver dem
data = data.drop(columns=['xkoord', 'ykoord'], errors='ignore')

# Ersätt specialtecken eller felaktiga tecken i datan
data = data.replace({'Ã¤': 'ä', 'Ã¶': 'ö', 'Ã¥': 'å'}, regex=True)

# Tar bort BOM från kolumnnamnen
if any('ï»¿' in col for col in data.columns):
	data.columns = data.columns.str.replace('ï»¿', '')

# Skapa en ny kolumn baserat på om ägaren är "VGR"

data['agare_vgr'] = np.where(data['agare'] == 'VGR', 'Ja', 'Nej')


total_sjukhus_per_agare = data.groupby('agare')['id'].count().reset_index(name='antal_sjukhus_per_agare')
data = data.merge(total_sjukhus_per_agare, on='agare', how='left')
total_sjukhus_per_agare = data.groupby('agare')['id'].transform('count')

# Lägg till resultatet som en ny kolumn
data['antal_sjukhus_per_agare'] = total_sjukhus_per_agare

#print(data)


#funerar toppen radera eller redigera inget

# Spara den rena datan till en ny CSV-fil
data.to_csv('sjukhus_clean.csv', index=False)

# Spara den rena datan till en ny Excel-file
data.to_excel('sjukhus_clean.xlsx', index=False)

# skapa en stapeldiagram som visar antal sjukhus per ägare '
# x-axeln visar ägare och y-axeln visar antal sjukhus

x = data['agare']
y = data['antal_sjukhus_per_agare']

plt.bar(x, y)
plt.xlabel('Ägare')
plt.ylabel('Antal sjukhus')
plt.title('Antal sjukhus per ägare')
plt.show()


# Räkna antal sjukhus per ort
x = data['postort'].value_counts().index  # Postort som etiketter
y = data['postort'].value_counts().values  # Antal sjukhus

# Skapa ett stapeldiagram
plt.bar(x, y)
plt.title('Placering av sjukhus')
plt.xlabel('Postort')
plt.ylabel('Antal sjukhus')
plt.xticks(rotation=45)  # Roterar x-axelns etiketter för bättre läsbarhet
plt.tight_layout()   # För att justera marginaler
plt.show()


