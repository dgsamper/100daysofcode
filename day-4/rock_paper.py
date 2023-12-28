import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list_of_possibilities = ["rock", "paper", "scissors"]
human = input("What do you choose? Rock, Paper or Scissors\n").lower()

if human not in list_of_possibilities:
    print("You chose the wrong option. Choose rock, paper or scissors!")
else:
    if human == "rock":
        print(rock)
    elif human == "paper":
        print(paper)
    elif human == "scissors":
        print(scissors)

    computer = random.choice(list_of_possibilities)

    print(f"Computer chose {computer}.")

    if computer == "rock":
        print(rock)
    elif computer == "paper":
        print(paper)
    elif computer == "scissors":
        print(scissors)
    # print(computer)


    if human != computer:
        if human == "rock" and computer == "scissors":
            print("You won!")
        elif human == "paper" and computer == "rock":
            print("You won!")
        elif human == "scissors" and computer == "paper":
            print("You won!")
        else:
            print("You lost!")
    else:
        print("That's a tie!")

