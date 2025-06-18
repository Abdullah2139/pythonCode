import random

print("Welcome to the PyPassword Generator!")

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()-+"

letter_count = int(input("How many letters would you like in your password?\n"))
number_count = int(input("How many numbers would you like in your password?\n"))
symbol_count = int(input("How many symbols would you like in your password?\n"))


password = ""
for char in range(0, letter_count):
    password += random.choice(letters)

for char in range(0, number_count):
    password += random.choice(numbers)

for char in range(0, symbol_count):
    password += random.choice(symbols)

print("Your simple password is:", password)

# Randomly shuffle the password to make it more secure

password = ''.join(random.sample(password, len(password)))
print(f"Your final shuffled password is: {password}")