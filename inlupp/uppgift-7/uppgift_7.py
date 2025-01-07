# Uppgift 7
# Skapa en funktion validate_password(password) som kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.

def validate_password(password):
    
    if len(password) < 8:
        return False
    
    if not any(char.isdigit() for char in password):
        return False
    
    return True


print(validate_password("viktoria"))
print(validate_password("biktoria1"))
print(validate_password("ciktor1"))

