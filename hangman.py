# This is an educational project by Todd Aitkins and is "Open Source" - 2020
# Some code is based on an educational project completed online at exercism.io

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

# Game status categories
STATUS_WIN = "won"
STATUS_LOSE = "lost"
STATUS_ONGOING = "playing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = ''.join(['_' for ltr in range(len(self.word))])
        self.guessed_list = []

    def guess(self, char):
        if self.status == STATUS_LOSE:
            raise ValueError("You can't guess if you already lost the game.")
        elif self.status == STATUS_WIN:
            raise ValueError("Please stop your guessing, you already won the game.")
        if char.isalpha() and len(char) == 1:  # A valid guess
            char = char.upper()
            self.guessed_list.append(char)  # Add letter to the list of guesses no matter if it was a good guess
            if char in self.masked_word:  # Guessing a correct letter again
                self.remaining_guesses -= 1
                if self.remaining_guesses < 0:
                    self.status = STATUS_LOSE
            elif char in self.word:
                self.update_masked_word(char)
                if self.word == self.masked_word:  # Check if word is solved
                    self.status = STATUS_WIN
            else:
                self.remaining_guesses -= 1
                if self.remaining_guesses < 0:
                    self.status = STATUS_LOSE
        else:
            raise Exception

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status

    def update_masked_word(self, char):
        self.masked_word = ''.join\
            ([char if self.word[i] == char else self.masked_word[i] for i in range(len(self.word))])

    # Define draw_man function
    def draw_man(self):
        if self.remaining_guesses >= 9:
            head = ""
            left_arm = ""
            right_arm = ""
            torso = ""
            left_leg_top = ""
            left_leg_bot = ""
            right_leg_top = ""
            right_leg_bot = ""
        elif self.remaining_guesses > 8:
            head = "O"
            left_arm = ""
            right_arm = ""
            torso = ""
            left_leg_top = ""
            left_leg_bot = ""
            right_leg_top = ""
            right_leg_bot = ""
        elif self.remaining_guesses > 6:
            head = "O"
            left_arm = "--+"
            right_arm = ""
            torso = ""
            left_leg_top = ""
            left_leg_bot = ""
            right_leg_top = ""
            right_leg_bot = ""
        elif self.remaining_guesses > 4:
            head = "O"
            left_arm = "--+"
            right_arm = "--"
            torso = ""
            left_leg_top = ""
            left_leg_bot = ""
            right_leg_top = ""
            right_leg_bot = ""
        elif self.remaining_guesses > 2:
            head = "O"
            left_arm = "--+"
            right_arm = "--"
            torso = "|"
            left_leg_top = ""
            left_leg_bot = ""
            right_leg_top = ""
            right_leg_bot = ""
        elif self.remaining_guesses > 0:
            head = "O"
            left_arm = "--+"
            right_arm = "--"
            torso = "|"
            left_leg_top = "/"
            left_leg_bot = ",/"
            right_leg_top = ""
            right_leg_bot = ""
        elif self.remaining_guesses <= 0:
            head = "O"
            left_arm = "--+"
            right_arm = "--"
            torso = "|"
            left_leg_top = "/"
            left_leg_bot = ",/"
            right_leg_top = "\\"
            right_leg_bot = '\\.'
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
        -------------\n".format(head, left_arm, right_arm, torso, left_leg_top, right_leg_top, left_leg_bot,
                                right_leg_bot))

    def draw_letterboard(self):
        print("Game status: {}".format(self.status))
        print("Letters guessed:  {}".format(', '.join(self.guessed_list)))
        print("Guesses remaining: {}".format(self.remaining_guesses + 1))
        print(' ' * 25, ' '.join([self.masked_word[ltr] for ltr in range(len(self.masked_word))]))


def draw_screen():
    print("\n\n\n\n")
    game.draw_man()
    game.draw_letterboard()


# Pick a word
def pick_word():
    return word_list[random.randrange(0, len(word_list))].upper()


# Make the game
game = Hangman(pick_word())

# Game Loop
draw_screen()
while game.status == STATUS_ONGOING:
    guessed_ltr = input("What is your guess?  ")  # Ask for Letter
    game.guess(guessed_ltr)
    draw_screen()
