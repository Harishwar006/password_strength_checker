# src/checks.py

def analyze_password(password):
    return {
        "length": len(password),
        "has_upper": any(c.isupper() for c in password),
        "has_lower": any(c.islower() for c in password),
        "has_digit": any(c.isdigit() for c in password),
        "has_special": any(not c.isalnum() for c in password),
        "is_common": password.lower() in [
            "password", "123456", "admin", "qwerty", "welcome"
        ]
    }
