# Uppgift 5
# Skapa en funktion filter_odd(numbers) som returnerar en lista med alla jämna tal från den givna listan.

def filter_odd(numbers):

    
    """
    
    Returnerar en lista med alla jämna tal från den givna listan.
    
    """
    
    return [numbers for numbers in numbers if numbers % 2 == 0]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(filter_odd(numbers)) 



