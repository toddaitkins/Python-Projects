# This is an educational project by Todd Aitkins and is "Open Source" - 2020

import random

# Define list of words
word_list = [
    "apple",
    "orange",
    "banana",
    "grape",
    "pencil",
    "cup",
    "basket"]

# Define list of guesses
guess_name = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh"]

guess_number = 0
secret_word = ""
secret_word_len = 0
guessed_letter = ""
guessed_list = []
my_guess = []


# Pick a word
def pick_word():
    global secret_word
    global secret_word_len
    global my_guess
    secret_word = word_list[random.randrange(0, len(word_list))].upper()
    secret_word_len = len(secret_word)

    for i in range(0, secret_word_len):  # Size the list with blanks according to the secret word picked
        my_guess.append(" ")


# Define draw_man function
def draw_man():
    if guess_number == 0:
        head = ""
        left_arm = ""
        right_arm = ""
        torso = ""
        left_leg_top = ""
        left_leg_bot = ""
        right_leg_top = ""
        right_leg_bot = ""
    elif guess_number == 1:
        head = "O"
        left_arm = ""
        right_arm = ""
        torso = ""
        left_leg_top = ""
        left_leg_bot = ""
        right_leg_top = ""
        right_leg_bot = ""
    elif guess_number == 2:
        head = "O"
        left_arm = "--+"
        right_arm = ""
        torso = ""
        left_leg_top = ""
        left_leg_bot = ""
        right_leg_top = ""
        right_leg_bot = ""
    elif guess_number == 3:
        head = "O"
        left_arm = "--+"
        right_arm = "--"
        torso = ""
        left_leg_top = ""
        left_leg_bot = ""
        right_leg_top = ""
        right_leg_bot = ""
    elif guess_number == 4:
        head = "O"
        left_arm = "--+"
        right_arm = "--"
        torso = "|"
        left_leg_top = ""
        left_leg_bot = ""
        right_leg_top = ""
        right_leg_bot = ""
    elif guess_number == 5:
        head = "O"
        left_arm = "--+"
        right_arm = "--"
        torso = "|"
        left_leg_top = "/"
        left_leg_bot = ",/"
        right_leg_top = ""
        right_leg_bot = ""
    elif guess_number == 6:
        head = "O"
        left_arm = "--+"
        right_arm = "--"
        torso = "|"
        left_leg_top = "/"
        left_leg_bot = ",/"
        right_leg_top = "\\"
        right_leg_bot = '\\.'
    elif guess_number == 7:
        pass
    else:
        pass

    print("\n\n\n\n\
          |--------------\n\
          |             |\n\
          |             -\n\
          |             {}\n\
          |           {}{}\n\
          |             {}\n\
          |            {} {}\n\
          |          {}   {}\n\
          |\n\
          |\n\
          |\n\
    -------------\n".format(head, left_arm, right_arm, torso, left_leg_top, right_leg_top, left_leg_bot, right_leg_bot))


def draw_letterboard():
    global guessed_list
    global secret_word_len
    global my_guess
    # Draw in guessed letters
    letters = ""
    for i in range(0, secret_word_len):
        letters = letters + "  " + my_guess[i] + "  "
    print("                {}\n".format(letters))
    # Draw blanks
    letterboard = ""
    for i in range(0, secret_word_len):
        letterboard = letterboard + "  ---"
    print("               {}\n".format(letterboard))
    print("Letters guessed: {}".format(guessed_list))


def draw_screen():
    print("\n\n\n\n")
    draw_man()
    draw_letterboard()


def check_guess_valid(guessed_letter):
    guessed_letter = guessed_letter.upper()
    if (len(guessed_letter) > 1) or (guessed_letter.isalpha() == False):
        return False
    else:
        for i in range(0, len(guessed_list)):
            if guessed_list[i] == guessed_letter:
                return False
        return True


def check_letter(guessed_letter):
    for i in range(0, secret_word_len):
        if guessed_letter == secret_word[i]:
            my_guess[i] = guessed_letter


def check_for_win():
    for i in range(0, secret_word_len):
        if my_guess[i] == " ":
            return False
    return True


# Game opening
print("Welcome to the hangman game!")

pick_word()

# Game Loop
while 1:
    draw_screen()
    if check_for_win():
        print("\nYou Won!!!!!!!!!!!!!!!!!!!!!!")
        break
    if guess_number >= 6:
        print("You ran out of luck.  He's dead!!!")
        print("\nR.I.P. Hangman...\n")
        break
    # Ask for Letter
    guessed_letter = input("What is your {} guess?  ".format(guess_name[guess_number]))
    guessed_letter = guessed_letter.upper()
    if not check_guess_valid(guessed_letter):
        print(
            "That's an invalid guess.  Please guess a LETTER and only ONE at a time, and please don't guess the same "
            "thing more than once.")
    else:
        guessed_list.append(guessed_letter)
        guess_number += 1
        check_letter(guessed_letter)
