# Uppgift 1
# Skapa en funktion is_odd(x) som returnerar True om x är udda och False om x är jämnt.
# def funktions_namn(variabel_namn: datatyp) -> returtyp:
# Exempel: def is_odd(x: int) -> bool:
# Förklaring: Funktionens namn är is_odd och tar en parameter x av datatypen int. Funktionen returnerar en bool.

def is_odd(number: int) -> bool:
    
    TrueOrFalse = (number % 2 == 0)
    
    return TrueOrFalse

print(is_odd(2))
print(is_odd(3))
print(is_odd(4))
print(is_odd(5))
print(is_odd(6))