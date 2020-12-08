import random

from typing import List

from words import WORD_LIST

def main():
    ATTEMPTS_ALLOWED = 6

    secret_word = get_random_word(WORD_LIST)

    correct_guesses = []
    incorrect_guesses = []
    lives = calc_attempts_remaining(ATTEMPTS_ALLOWED, incorrect_guesses)

    result = None
    while result is None:

        print(print_lives_left(lives))
        blanked_word = reveal_letters(secret_word, correct_guesses)
        print(blanked_word)
        print()

        # get guess
        guess = get_guess(correct_guesses + incorrect_guesses)

        if letter_is_in_word(guess, secret_word):
            print("That is correct!")
            correct_guesses.append(guess)
        else:
            print("Incorect.")
            incorrect_guesses.append(guess)
        
        lives = calc_attempts_remaining(ATTEMPTS_ALLOWED, incorrect_guesses)
        
        if all_letters_present_in_list(secret_word, correct_guesses):
            result = "win"
        elif lives <= 0:
            result = "lose"

    print(word_reveal_message(secret_word))
    print(outcome_message(result))


def get_random_word(word_list):
    return random.choice(word_list)


def print_lives_left(lives):
    return f"you have {lives} out of 6 lives left"


def reveal_letters(word, visible_letters):
    hidden_word = ""
    for letter in word:
        if letter in visible_letters:
            hidden_word += letter
        else:
            hidden_word += "_"
        hidden_word += " "
    return hidden_word.strip()


def word_reveal_message(word):
    return f"The secret word was '{word}'."


def calc_attempts_remaining(attempts_allowed, incorrect_guesses):
    remaining_attempts = attempts_allowed - len(incorrect_guesses)
    return remaining_attempts


def letter_is_in_word(letter, word):
    return letter in word


def all_letters_present_in_list(word, letter_list):
    for i in range(len(word)):
        if word[i] not in letter_list:
            return False
    return True
  

def outcome_message(result):
    if result == "win":
        return "You have won."
    else:
        return "You have lost."

def get_guess(all_guesses):
    
    valid = False
    while valid is False:
        letter = input("Please enter a letter to guess: ")
        if letter not in all_guesses and len(letter) == 1 and letter.isalpha():
            return letter
        elif letter in all_guesses:
            print("ALREADY GUESSED!")
        elif len(letter) != 1:
            print("INVALID GUESS!")
        else:
            print("NOT A LETTER!")
        print()

if __name__ == "__main__":
    main()
