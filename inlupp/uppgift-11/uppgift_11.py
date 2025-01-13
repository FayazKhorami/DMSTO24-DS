# Uppgift 11
# Skapa en funktion word_count(text) som returnerar antalet ord i en given text.

def word_count(text):

    """

    Returnerar antalet ord i en skrivit text.

    """

    count = 0

    # Dela texten i ord baserat på mellanslag
    words = text.split()  
    for word in words:
    
        # Räkna antalet ord
        count += 1
    
    return count


print(word_count("Det här är ett exempel."))
print(word_count("hello world"))
print(word_count(""))
print(word_count("Python är fantastiskt!"))


