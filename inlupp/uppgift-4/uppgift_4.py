# Uppgift 4
# Skapa en funktion fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.


def fibonacci(n):
    
    """
    
    Returnerar en lista med de första n Fibonacci-talen.
    
    """
    if n <= 0:
        return []  
    elif n == 1:
        return [0]  
    
    
    fib_sequence = [0, 1]
    
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence


n = 10
print(fibonacci(n)) 
