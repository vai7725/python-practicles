import re

# Validate an email address
email = "example@example.com"
email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
email_valid = bool(re.match(email_regex, email))

# Validate a phone number (US format)
phone = "(123) 456-7890"
phone_regex = r"^\(\d{3}\) \d{3}-\d{4}$"
phone_valid = bool(re.match(phone_regex, phone))

# Validate a password (at least 8 characters, 1 uppercase, 1 lowercase, 1 number)
password = "Password123"
password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$"
password_valid = bool(re.match(password_regex, password))

# Validate a date (YYYY-MM-DD)
date = "2024-12-06"
date_regex = r"^\d{4}-\d{2}-\d{2}$"
date_valid = bool(re.match(date_regex, date))

print(f"Email valid: {email_valid}")
print(f"Phone valid: {phone_valid}")
print(f"Password valid: {password_valid}")
print(f"Date valid: {date_valid}")
