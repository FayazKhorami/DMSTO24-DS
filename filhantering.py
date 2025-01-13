

#öppna en fil med context manager (i skrivläge = "W")
with open ("data.csv", "w") as file:
    # Vi skriver till filen, rad 1, rubrikerna:
    
    file.write("Name, Age, City\n")
# Nu är filen stängd

# Vi öppnar filen igen
with open("data.csv", "a") as file:

    file.write("Anna, 34, Stockholm\n")
    
    file.write("björn, 23, Göteborg\n")
    
    file.write("Kalle, 45, Uppsala")
    
# Nu är filen stängd

# Öppna i läsläge hela filen
with open("data.csv", "r") as file:
    
    print(file.read())

