# Uppgift 3
# Hitta det största talet i en lista


def max_in_list(numbers):
    
    """
    
    Returnerar det största talet i listan.
    
    """
    
    if not numbers:
        raise ValueError("Listan får inte vara tom.")
    return max(numbers)


numbers = [3, 7, 2, 8, 4, 10, 100, 255, 655, 800, 999999, 6]

print(max_in_list(numbers))  




