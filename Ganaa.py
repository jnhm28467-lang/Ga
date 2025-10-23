# Function to check password strength
def check_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_symbol = True

    if len(password) >= 8 and has_upper and has_lower and has_digit and has_symbol:
        return True
    else:
        return False


# Function to make the password stronger
def make_strong_password(password):
    while len(password) < 8:
        password += "x"

    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_symbol = any(not ch.isalnum() for ch in password)

    if not has_upper:
        password += "A"
    if not has_lower:
        password += "a"
    if not has_digit:
        password += "1"
    if not has_symbol:
        password += "@"

    return password


# Main part
password = input("Enter your password: ")

if check_password(password):
    print("✅ Password is strong!")
else:
    print("⚠️ Password is weak!")
    new_pass = make_strong_password(password)
    print("💡 Suggested strong password:", new_pass)
