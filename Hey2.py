import re

def is_strong_password(password):
    # Check if the password has at least 8 characters.
    if len(password) < 8:
        return False
    
    # Check if the password contains at least one lowercase letter.
    if not any(char.islower() for char in password):
        return False
    
    # Check if the password contains at least one uppercase letter.
    if not any(char.isupper() for char in password):
        return False
    
    # Check if the password contains at least one digit.
    if not any(char.isdigit() for char in password):
        return False
    
    # Check if the password contains at least one special character.
    if not re.search(r'[!@#$%^&*()\-+]', password):
        return False
    
    # Check if the password does not contain 2 of the same characters in adjacent positions.
    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            return False
    
    return True

# Read input
passwords = input().split()

# Check each password and print 'true' or 'false' without any separator
for password in passwords:
    if is_strong_password(password):
        print('true ', end='')
    else:
        print('false ', end='')
