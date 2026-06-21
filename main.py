import string

# List of common passwords
common_passwords = [
    "123456",
    "password",
    "admin",
    "qwerty",
    "abc123",
    "password123",
    "welcome",
    "letmein",
    "iloveyou",
    "123456789"
]

# Take password input
password = input("Enter your password: ")

score = 0

# Check password length
if len(password) >= 8:
    score += 1

# Check uppercase
if any(char.isupper() for char in password):
    score += 1

# Check lowercase
if any(char.islower() for char in password):
    score += 1

# Check digits
if any(char.isdigit() for char in password):
    score += 1

# Check special characters
if any(char in string.punctuation for char in password):
    score += 1

print("\nPassword Score:", score)

# Password Strength
if score <= 2:
    print("Password Strength: Weak")
elif score == 3 or score == 4:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")

# Check common password
if password.lower() in common_passwords:
    print("\n⚠ WARNING!")
    print("This is a very common password.")
    print("Hackers can easily guess it.")

# Suggestions
print("\nSuggestions:")

if len(password) < 8:
    print("• Increase password length to at least 8 characters.")

if not any(char.isupper() for char in password):
    print("• Add at least one uppercase letter.")

if not any(char.islower() for char in password):
    print("• Add at least one lowercase letter.")

if not any(char.isdigit() for char in password):
    print("• Add at least one number.")

if not any(char in string.punctuation for char in password):
    print("• Add at least one special character.")

if score == 5 and password.lower() not in common_passwords:
    print("✅ Excellent! Your password is very strong.")