# Uppgift 7
# Skapa en funktion validate_password(password) som kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.

def validate_password(password):
    
    """
    
    Kollar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.
    Returnerar True om lösenordet är giltigt, annars False.
    
    """
    
    if len(password) < 8:
        return False  # Lösenordet är för kort
    
    if not any(char.isdigit() for char in password):
        return False
    
    return True


print(validate_password("password"))
print(validate_password("password123"))
print(validate_password("pass1"))
