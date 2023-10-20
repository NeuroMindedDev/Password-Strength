import re

def is_strong_password(password):
    # At least 8 characters
    if len(password) < 8:
        return False

    # Contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Contains at least one digit
    if not re.search(r'[0-9]', password):
        return False

    # Contains at least one special character (e.g., !, @, #, etc.)
    if not re.search(r'[!@#$%^&*()_+]', password):
        return False

    return True

def main():
    password = input("Enter a password: ")
    
    if is_strong_password(password):
        print("Strong password! Good job.")
    else:
        print("Weak password. Please choose a stronger one.")

if __name__ == "__main__":
    main()
