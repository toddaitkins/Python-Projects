# This is an educational project by Todd Aitkins and is "Open Source" - 2020

import random

password_len = 0
is_password_len_valid = False
is_password_composition_valid = False
password_min_len = 6
password_max_len = 100
amount_letters = 0
amount_numbers = 0
amount_symbols = 0
password_original = []
password_scrambled = ""
have_valid_password = False

# Define list_letters
list_letters = []

# Make a list of all lowercase letters append to list_letters
letter = 'a'
for i in range(0, 26):
    list_letters.append(letter)
    letter = chr(ord(letter) + 1)

# Add all uppercase letters to list_letters
letter = 'A'
for i in range(0, 26):
    list_letters.append(letter)
    letter = chr(ord(letter) + 1)

# Make a list of numbers 0 - 9
list_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Make a list of the symbols to be used
list_symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

print("This is a simple random password generator program.")

# Ask user for the desired password length and then check if it's 6 - 100 to be valid
password_len = int(input("How long of a password would you like to generate?\nIt must be at least 6 and no more than "
                         "100 characters.  "))

# While loop checking is_password_len_valid
while not is_password_len_valid:
    if password_len is None:
        # No response
        print("\nThat is a terrible answer!  Did you even type a number?")
    elif (password_len >= password_min_len ) and (password_len <= password_max_len):
        # password_len is valid and we reassure the user
        print("\nThat is a great password length!")
        is_password_len_valid = True
    else:
        # password_len outside the valid range
        print("\nI'm sorry but {} is simply outside the range that I can generate.\nPlease try again.".format(password_len))
        password_len = int(input("\nLet's try this again.  How long would you like?\n(Hint: somewhere between 6 and "
                                 "100.)"))

# While loop checking is_password_composition_valid
while not is_password_composition_valid:
    # Ask user how many letters
    amount_letters = int(input("How many letters would you like?  "))
    # Ask user how many numbers
    amount_numbers = int(input("How many numbers would you like?  "))
    # Ask user how many special symbols
    amount_symbols = int(input("How many symbols would you like?  "))
    # Check if the sum is equal to the desired length.  If not we'll just generate an error and tell the user its wrong.
    if (amount_letters + amount_numbers + amount_symbols) == password_len:
        # Composition check appears to match the desired length.
        print("You entered: {} letters; {} numbers; {} symbols which equals a total length of {}.".format(amount_letters, amount_numbers, amount_symbols, password_len))
        is_password_composition_valid = True
    else:
        # something is wrong
        print("\nI'm sorry but you entered something invalid and therefore I can't generate.  Please try again.\n")

# Make the password

# Pick amount_letters from list and append them to password_original
for i in range(0, amount_letters):
    password_original.append(list_letters[random.randrange(0, len(list_letters))])

# Pick amount_numbers from list and append them to password_original
for i in range(0, amount_numbers):
    password_original.append(list_numbers[random.randrange(0, len(list_numbers))])

# Pick amount_symbols from list and append them to password_original
for i in range(0, amount_symbols):
    password_original.append(list_symbols[random.randrange(0, len(list_symbols))])

# Randomize the list of characters
random.shuffle(password_original)

# Convert the list of values into a single concatenated string
for i in range(0, len(password_original)):
    password_scrambled = password_scrambled + str(password_original[i])

# Display final string to user
print("\nYou're new password is:  {}".format(password_scrambled))














