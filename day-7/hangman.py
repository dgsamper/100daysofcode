import random
import hangman_art as ha
import hangman_words as hw
import os

chosen_word = random.choice(hw.word_list)
lives = 6

print(ha.logo)

display = []
for letter in range(len(chosen_word)):
    display.append("_")

guessed_letters = []
while "_" in display:
    
    guess = input("Guess a letter: ").lower()
    os.system('clear')

    # checks if the letter already be guessed
    if guessed_letters.count(guess) > 0:
        print(f"You already guessed the letter {guess}. Choose another letter.")
    else:
        guessed_letters.append(guess)
        # checks if the letter is not in the list. if is not, decrement the lives
        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = guess            

    print(f"{' '.join(display)}")
    print(ha.stages[lives])

    if lives == 0:
        print("You lost!")
        break

if "_" not in display:
    print("You won!")