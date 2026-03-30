# password_analyzer.py
# Simple Password Strength Analyzer
# CYB 333 - Security Automation Project

def check_length(password):
    """Check if password is at least 8 characters."""
    return len(password) >= 8

def has_lowercase(password):
    """Check if password has at least one lowercase letter."""
    return any(char.islower() for char in password)

def has_uppercase(password):
    """Check if password has at least one uppercase letter."""
    return any(char.isupper() for char in password)

def has_digit(password):
    """Check if password has at least one number."""
    return any(char.isdigit() for char in password)

def has_special_char(password):
    """Check if password has at least one special character."""
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    return any(char in special_chars for char in password)

def score_password(password):
    """
    Score the password and return strength rating.
    Returns: (rating, score, failed_checks)
    """
    checks = {
        'Length (8+ characters)': check_length(password),
        'Has lowercase letter': has_lowercase(password),
        'Has uppercase letter': has_uppercase(password),
        'Has number': has_digit(password),
        'Has special character': has_special_char(password),
    }
    
    # Count how many checks passed
    passed = sum(checks.values())
    
    # Determine rating
    if passed <= 2:
        rating = "WEAK"
    elif passed <= 4:
        rating = "MEDIUM"
    else:
        rating = "STRONG"
    
    # Get failed checks for suggestions
    failed = [check for check, result in checks.items() if not result]
    
    return rating, passed, failed, checks

def main():
    """Main program."""
    print("=" * 50)
    print("PASSWORD STRENGTH ANALYZER")
    print("=" * 50)
    
    password = input("\nEnter a password to check: ")
    
    rating, score, failed, checks = score_password(password)
    
    print("\n" + "=" * 50)
    print(f"Password Strength: {rating}")
    print(f"Score: {score}/5 checks passed")
    print("=" * 50)
    
    print("\nCheck Results:")
    for check_name, result in checks.items():
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"  {status} - {check_name}")
    
    if failed:
        print("\nSuggestions to improve:")
        for i, suggestion in enumerate(failed, 1):
            print(f"  {i}. Add: {suggestion.lower()}")
    else:
        print("\n✓ Your password is strong!")
    
    print("=" * 50)

if __name__ == "__main__":
    main()
