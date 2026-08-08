#  Create a game that say Welcome Code breaker! Lets see if you can my 3 digit number. You have 10 attempts to guess the number.
#   The number is generated randomly and you have to guess the number. And you have to guess a 3 digit number.
#   What is your guess?
#   Here is the result of your guess:
#   Match
#   And repeat those questions 2 times more if you choose the correct answer.

import random

def guess_number():
    number = random.randint(100, 999)
    print(number)
    return number

def guess_number_game():
    number = guess_number()
    guess = int(input("What is your guess? "))
    if guess == number:
        print("You guessed the number!")
    else:
        print("You guessed the number!")