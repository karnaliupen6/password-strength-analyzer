# Password Strength Analyzer
# Course: CYB 333 - Security Automation
# Author: karnaliupen6
# This program checks how strong a password is and tells the user what to improve

# These are the special characters we check for
SPECIAL_CHARACTERS = "!@#$%^&*"

# Check if the password is at least 8 characters long
def check_length(password):
    return len(password) >= 8

# Check if the password has at least one lowercase letter
def check_lowercase(password):
    return any(char.islower() for char in password)

# Check if the password has at least one uppercase letter
def check_uppercase(password):
    return any(char.isupper() for char in password)

# Check if the password has at least one number
def check_number(password):
    return any(char.isdigit() for char in password)

# Check if the password has at least one special character
def check_special_character(password):
    return any(char in SPECIAL_CHARACTERS for char in password)

# Give a rating based on how many checks passed
# 5 = Strong, 3 or 4 = Moderate, anything below = Weak
def get_strength_rating(score):
    if score == 5:
        return "STRONG"
    elif score >= 3:
        return "MODERATE"
    else:
        return "WEAK"

# Run all the checks and print the results
def analyze_password(password):
    print("=" * 50)

    # List of all checks - each one has a name and a result (True or False)
    results = [
        ("Length (8+ characters)", check_length(password)),
        ("Has lowercase letter",   check_lowercase(password)),
        ("Has uppercase letter",   check_uppercase(password)),
        ("Has number",             check_number(password)),
        ("Has special character",  check_special_character(password)),
    ]

    # Count how many checks passed
    score = sum(1 for _, passed in results if passed)

    # Get the strength label
    strength = get_strength_rating(score)

    # Show the overall result
    print(f"Password Strength: {strength}")
    print(f"Score: {score}/5 checks passed")
    print("=" * 50)

    # Show which checks passed and which failed
    print("\nCheck Results:")
    for check_name, passed in results:
        status = "PASS" if passed else "FAIL"
        symbol = "✓" if passed else "✗"
        print(f"  {symbol} {status} - {check_name}")

    # Print a final message based on the rating
    print()
    if strength == "STRONG":
        print("Your password is strong!")
    elif strength == "MODERATE":
        print("Your password is moderate. Try adding more variety.")
    else:
        print("Your password is weak. Please make it stronger.")

    print("=" * 50)

# This is where the program starts
# Ask the user to type a password and run the analysis
if __name__ == "__main__":
    print("=" * 50)
    print("PASSWORD STRENGTH ANALYZER")
    print("=" * 50)

    # Get the password from the user
    user_password = input("\nEnter a password to check: ")

    print()

    # Run all the checks on the password
    analyze_password(user_password)
