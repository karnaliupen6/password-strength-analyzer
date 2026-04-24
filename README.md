# Password Strength Analyzer

## Project Description

This project is a simple Python security automation tool that analyzes password strength and provides suggestions for improvement. It demonstrates how password security checks can be automated using Python as part of CYB 333 Security Automation.

## Objectives

- Automate password strength evaluation
- Apply basic cybersecurity password rules
- Provide user-friendly feedback on password quality
- Demonstrate Python scripting for security automation

## Features

- Checks whether the password is at least 8 characters long
- Checks for lowercase letters
- Checks for uppercase letters
- Checks for numbers
- Checks for special characters
- Displays an overall rating: Weak, Moderate, or Strong
- Shows detailed pass/fail results for each rule
- Provides a final message based on password strength

  ## Why These Five Rules?

The reason I chose these five validation rules is that they are the most common password security guidelines in the industry:

- **Length (8+ characters)** — Makes brute forcing harder by increasing the number of combinations that attackers have to try
- **Lowercase letters** — Ensures basic character variety and is required by most password policies
- **Uppercase letters** — Boosts entropy and makes the password more complicated
- **Numbers** — Adds numeric element, which decreases the effectiveness of dictionary attacks
- **Special characters** — Make the password very strong, as they increase the character set to a large extent

There are other ways, e.g., by checking a password's entropy or by matching it against a list of compromised passwords. Still, my rule-based approach was suitable for this automation project because it is deterministic, straightforward to test, and it makes it very clear to the users what their next step is.

## Requirements

- Python 3.6 or higher
- No external libraries required
- Uses only the Python standard library

## Installation

```bash
git clone https://github.com/karnaliupen6/password-strength-analyzer.git
cd password-strength-analyzer
```

## Usage

Run the program with:

```bash
python password_analyzer.py
```

Then enter a password when prompted.

## Example Output

```text
==================================================
PASSWORD STRENGTH ANALYZER
==================================================

Enter a password to check: Driver#456

==================================================
Password Strength: STRONG
Score: 5/5 checks passed
==================================================

Check Results:
  ✓ PASS - Length (8+ characters)
  ✓ PASS - Has lowercase letter
  ✓ PASS - Has uppercase letter
  ✓ PASS - Has number
  ✓ PASS - Has special character

Your password is strong!
==================================================
```

## File Information

- `password_analyzer.py` — main Python program for password strength analysis
- `README.md` — project documentation and instructions

## Course Information

- Course: CYB 333 - Security Automation
- Author: karnaliupen6
- Project Type: Individual course project

## Future Improvements

- Check passwords against common breach databases
- Add GUI support using tkinter
- Create a web version using Flask
- Add support for checking multiple passwords from a file
- Integrate with system password managers

## License

This project is open source and intended for educational purposes.
