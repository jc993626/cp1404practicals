"""
On paper, write a program that asks the user for a password,
with error-checking to repeat if the password doesn't meet a minimum length set by a variable.
The program should then print asterisks as long as the word.
Example: if the user enters Pythonista (10 characters), the program should print **********.
"""
min_password_length = int(input("Enter minimum password length:"))
password = str(input("Please enter password:"))

while len(password) < min_password_length or len(password) > min_password_length:
    print(f"Password length incorrect, must be {min_password_length} characters long")
    password = str(input("Enter password:"))

print("*" * min_password_length)


