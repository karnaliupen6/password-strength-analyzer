# Password Strength Analyzer

## Project Description

A simple Python security automation tool that analyzes password strength and provides suggestions for improvement. This project demonstrates automated password security evaluation, a key component of security automation.

## Features

- **Automated Password Checking**: Evaluates passwords against multiple security rules
- **Strength Rating**: Provides clear feedback (Weak, Medium, Strong)
- **Improvement Suggestions**: Shows specific recommendations for strengthening weak passwords
- **Rule-Based Scoring**: Checks for:
  - Minimum length (8+ characters)
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Special characters (!@#$%^&*)

## Installation

No external dependencies required. Uses only Python standard library.

requirements: Python 3.6 or higher

```bash
git clone https://github.com/karnaliupen6/password-strength-analyzer.git
cd password-strength-analyzer
```

## Usage

```bash
python password_analyzer.py
```

Then enter a password when prompted.

### Example

```
==================================================
PASSWORD STRENGTH ANALYZER
==================================================

Enter a password to check: MyPass123!

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

## Project Goals

This project demonstrates:
- Security automation principles
- Automated security best practice enforcement
- Python programming fundamentals
- Clear code documentation and comments

## Course Information

- **Course**: CYB 333 - Security Automation
- **Author**: karnaliupen6
- **Status**: complete

## Future Improvements

- Check passwords against common breach databases
- Add GUI interface with tkinter
- Create web-based version with Flask
- Add support for checking multiple passwords from file
- Integrate with system password managers

## License

Open source - for educational purposes
