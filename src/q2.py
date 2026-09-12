"""HW1 Question 2"""

def validate_password(password: str) -> bool:
    if len(password) < 8:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True
    """Variable to check if all conditions are met"""
    valid_password = has_upper and has_lower and has_digit and has_special
    return valid_password

