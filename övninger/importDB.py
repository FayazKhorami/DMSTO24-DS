

import pandas as pd
import psycopg2


# Anslut till PostgreSQL-databasen

conn = psycopg2.connect (

    host="*****",   # Byt ut med din värd

    database="postgres",    # Byt ut med din databas

    user="postgres",    # Byt ut med ditt användarnamn

    password="********",  # Byt ut med ditt lösenord

    port="5432"  # Byt ut med din port (oftast 5432 för PostgreSQL

)


cursor = conn.cursor()

# Läs in CSV-filen

csv_file_path = "övninger\sales_data.csv"  # Sökvägen till din CSV-fil

df = pd.read_csv(csv_file_path)

# Skapa tabellen i PostgreSQL om den inte redan finns
# Man måste skapa en schema för att kunna skapa en tabell i mitt fall jag skapade schemat jag och leder 
# till tabellen jag.sales 

create_table_query = """ 

    CREATE TABLE IF NOT EXISTS jag.sales (          
    id SERIAL PRIMARY KEY,
    date DATE,
    product VARCHAR(50),
    price NUMERIC,
    quantity INTEGER,
    sales NUMERIC

);
"""

cursor.execute(create_table_query)

conn.commit()

# Iterera genom DataFrame och lägg till data i tabellen

for index, row in df.iterrows():

    insert_query = """

    INSERT INTO jag.sales (date, product, price, quantity)
    VALUES (%s, %s, %s, %s)

"""

# Samma sak här jag skapade en ny schema för att kunna lägga till data i tabellen sales den schema kommer innan
# på csv filen alltså jag.sales

    cursor.execute(insert_query, (row['Date'], row['Product'], row['Price'], row['Quantity']))

# Spara ändringar i databasen

conn.commit()

# Stäng anslutningen

cursor.close()

conn.close()

print("CSV-filen har importerats till PostgreSQL!")

