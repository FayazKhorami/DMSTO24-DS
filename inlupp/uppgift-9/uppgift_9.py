# Uppgift 9
# Skapa en funktion is_palindrome(string) som kontrollerar om en given sträng är ett palindrom (dvs. samma framifrån och bakifrån).

def is_palindrome(string):

    # Tar bort alla teken som inte är bokstäver eller siffror och gör alla bokstäver små

    clean_string = ""
    for char in string:
        if char.isalnum():
            clean_string += char.lower()

    # kollar om clean_string är ett palindrom

    left, right = 0, len(clean_string) - 1
    while left < right:
        if clean_string[left] != clean_string[right]:
            return False
        left += 1
        right -= 1
    
    return True


print(is_palindrome("Anna"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome(""))
print(is_palindrome("radar"))
print(is_palindrome("python"))




