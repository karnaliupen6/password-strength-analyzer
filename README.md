# Password Strength Analyzer

## What This Project Does

This small Python program checks how strong your password is and tells 
you what you need to improve. It was built as part of a security 
automation course to show how security checks can be written and run 
automatically through code.

## Features

- Checks your password against common security rules
- Gives you a rating — Weak, Medium, or Strong
- Lets you know exactly what is missing so you can fix it
- Checks for:
  - Minimum 8 characters
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Special characters like !@#$%

## How to Install

No extra libraries needed. Just Python.

Requirements: Python 3.6 or higher

```bash
git clone https://github.com/karnaliupen6/password-strength-analyzer.git
cd password-strength-analyzer
```

## How to Run

```bash
python password_analyzer.py
```

Type a password when it asks you and press Enter.

## Example
==================================================
PASSWORD STRENGTH ANALYZER
==================================================

Enter a password to check: MyPass123!

==================================================
Password Strength: STRONG
Score: 5/5 checks passed
==================================================

Check Results:
PASS - Length (8+ characters)
PASS - Has lowercase letter
PASS - Has uppercase letter
PASS - Has number
PASS - Has special character

Your password is strong!
==================================================


## What This Project Covers

- Security automation using Python
- Enforcing password security rules through code
- Writing clean and well-commented Python scripts
- Using GitHub to manage and share a project

## Course Info

- Course: CYB 333 - Security Automation
- Author: karnaliupen6
- Status: Complete

## Ideas for Future Updates

- Check if a password has appeared in a data breach
- Add a simple visual interface using tkinter
- Build a web version using Flask
- Allow checking a whole list of passwords from a file
- Connect it to a password manager

## License

Open source — built for educational purposes.
