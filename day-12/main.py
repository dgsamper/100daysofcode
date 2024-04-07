# guess the number

import random

print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a numver between 1 and 100!!")

difficulty = input("Choose a difficult: Type 'easy' or 'hard':\n")
attempts = 0

def the_difficulty():
    if difficulty == "easy":
        return attempts + 10
    elif difficulty == "hard":
        return attempts + 5
    

def create_the_number():
    number = random.randint(1,101)
    return number

def main(attempts):
    while attempts > 0:
        print(f"You have {attempts} remaining to guess the number!\n")
        guess = int(input("Make a guess:\n"))
        if guess > number:
            print("Too high! Guess again!")
        elif guess < number:
            print("Too low! Guess again!")
        else:
            print("You guessed right. Congrats!")
            break    
        attempts -= 1
        if attempts == 0:
            print("You've run out of guesses, you lose.")


attempts = the_difficulty()
number = create_the_number()
main(attempts)