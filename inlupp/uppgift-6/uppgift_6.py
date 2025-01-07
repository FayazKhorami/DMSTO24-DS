# Uppgift 6
# Skapa en funktion multiplication_table(n, limit) som returnerar multiplikationstabellen för n upp till limit i en lista.


def multiplication_table(n, limit):
    
    """
    
    Returnerar multiplikationstabellen för n upp till limit i en lista.
    
    """
    
    if limit <= 0:
        raise ValueError("Limit måste vara ett positivt heltal.")
    
    return [n * i for i in range(1, limit + 1)]


n = 5

limit = 10

print(multiplication_table(n, limit))  
