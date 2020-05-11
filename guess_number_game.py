# This is an educational project by Todd Aitkins and is "Open Source" - 2020

import random

# Declare variables to use
have_valid_number = False
is_guess_correct = False
number_of_guesses = 1
secret_number = -1

# Loop until we have a valid number
while not have_valid_number:
    secret_number = int((random.random() * 100) / 5)  # Generate a random number from 0 - 20
    if 0 <= secret_number <= 20:  # Check if the number is outside our range by chance and try again
        have_valid_number = True
        print("I have a secret number between 0 and 20.  Do you want to guess it?")


while not is_guess_correct:  # Loop until we get a correct answer
    guess_number = int(input("\nWhat do you think the number is? "))
    if guess_number == secret_number:
        # A correct guess
        print("You guessed {}, that was my secret number that I was thinking of!  It took you {} guesses.".format(
            guess_number, number_of_guesses))
        is_guess_correct = True  # Set parameter to True to stop looping the game
    elif guess_number != secret_number:
        number_of_guesses += 1  # An incorrect guess, increment number_of_guesses
        if guess_number > secret_number:  # Check if too high
            print("You guessed {} which is too HIGH!".format(guess_number))
        elif guess_number < secret_number:  # Check if too low
            print("You guessed {} which is too LOW!".format(guess_number))
        else:  # This case shouldn't happen
            print("\nError:  Something happened very bad who programmed this awful mess.")
    else:  # This case shouldn't happen - including for educational purposes
        print("\nError:  Something happened very bad and I forgot the number I was thinking of.")

# Close out the game with a remark
print("\nThanks for playing with me!  Try again sometime.")
