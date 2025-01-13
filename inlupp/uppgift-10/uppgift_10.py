# Uppgift 10
# Skapa en funktion celsius_to_fahrenheit(celsius) som konverterar en temperatur från Celsius till Fahrenheit.

def celsius_to_fahrenheit(celsius):

    """

    Konverterar en temperatur från Celsius till Fahrenheit.

    """
    factor = 9 / 5
    offset = 32
    fahrenheit = celsius * factor + offset
    return fahrenheit


print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(25))
print(celsius_to_fahrenheit(-10))
print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))
print(celsius_to_fahrenheit(-40) == -40)



