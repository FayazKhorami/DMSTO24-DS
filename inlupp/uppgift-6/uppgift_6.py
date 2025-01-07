# Uppgift 6
# Skapa en funktion multiplication_table(n, limit) som returnerar multiplikationstabellen för n upp till limit i en lista. 


def multiplication_table(n, limit):
    
    if limit <= 0:
    
        return "Limit måste vara ett positivt heltal."
    table = []
    
    for i in range(1, limit + 1):
        table.append(n * i)
    
    return table

n = 5

limit = 10

print(multiplication_table(n, limit))
