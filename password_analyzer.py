# password_analyzer.py
# Simple Password Strength Analyzer
# CYB 333 - Security Automation Project

from getpass import getpass
import string

def check_length(password):
    """Return True if password is at least 8 characters long."""
    return len(password) >= 8

def has_lowercase(password):
    """Return True if password contains at least one lowercase letter."""
    return any(char.islower() for char in password)

def has_uppercase(password):
    """Return True if password contains at least one uppercase letter."""
    return any(char.isupper() for char in password)

def has_digit(password):
    """Return True if password contains at least one digit."""
    return any(char.isdigit() for char in password)

def has_special_char(password):
    """Return True if password contains at least one special character."""
    return any(char in string.punctuation for char in password)

def score_password(password):
    """
    Analyze the password and return:
    rating, score, failed_checks, all_check_results
    """
    checks = {
        "Length (8+ characters)": check_length(password),
        "Has lowercase letter": has_lowercase(password),
        "Has uppercase letter": has_uppercase(password),
        "Has number": has_digit(password),
        "Has special character": has_special_char(password),
    }

    score = sum(checks.values())

    if score <= 2:
        rating = "WEAK"
    elif score <= 4:
        rating = "MEDIUM"
    else:
        rating = "STRONG"

    failed_checks = [name for name, passed in checks.items() if not passed]
    return rating, score, failed_checks, checks

def main():
    print("=" * 50)
    print("PASSWORD STRENGTH ANALYZER")
    print("=" * 50)

    password = getpass("\nEnter a password to check: ").strip()

    if not password:
        print("\nError: Password cannot be blank.")
        return

    rating, score, failed, checks = score_password(password)

    print("\n" + "=" * 50)
    print(f"Password Strength: {rating}")
    print(f"Score: {score}/5 checks passed")
    print("=" * 50)

    print("\nCheck Results:")
    for check_name, result in checks.items():
        status = "PASS" if result else "FAIL"
        print(f"  {status} - {check_name}")

    if failed:
        print("\nSuggestions to improve:")
        for i, suggestion in enumerate(failed, 1):
            print(f"  {i}. {suggestion}")
    else:
        print("\nYour password is strong!")

    print("=" * 50)

if __name__ == "__main__":
    main()
