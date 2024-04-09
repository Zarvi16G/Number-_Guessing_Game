import random


def attemps(difficult):
    if difficult == 'hard':
        tries = 10
    else:
        tries = 5
    return tries


def process_game(number, user_number, tries):
    if user_number > number:
        print("Too high")
        tries -= 1
    elif user_number < number:
        print("Too low")
        tries -= 1


number = random.choice(range(1, 100))
print("Welcome to the Number Guessing Game \n")

while True:
    difficult = input("Choose the difficult, type 'easy' or 'hard: \n").lower()
    if difficult == 'easy' or difficult == 'hard':
        break
    else:
        print("Something going wrong")

tries = attemps(difficult)

while True:
    if tries != -1:
        user_number = int(input("Type the number to guess: \n"))
        print(tries)
        process_game(number, user_number, tries)
        if number == user_number:
            print("User has a victory")
            break
        else:
            tries -= 1
    else:
        print("You lost")
        break
