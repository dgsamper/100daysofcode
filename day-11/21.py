############### Blackjack Project #####################
import random
import util as u

def give_cards(deck, hand, number_of_cards):
    for _ in range(number_of_cards):
        hand.append(random.choice(deck))


def check_blackjack(hand):
    return sum(hand) == 21 and len(hand) == 2

def check_over_21(hand):
    if sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1
    return sum(hand) > 21


def current_round():
    print(u.logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_hand = []
    computer_hand = []

    give_cards(cards, user_hand, 2)
    give_cards(cards, computer_hand, 2)

    while True:
        print(f"Your cards: {user_hand}, current score: {sum(user_hand)}")
        print(f"Computer's first card: {computer_hand[0]}")

        if check_blackjack(user_hand):
            print("Blackjack! You win!")
            return
        if check_blackjack(computer_hand):
            print("Computer got a Blackjack! You lose!")
            return

        if check_over_21(user_hand):
            print("You went over 21! You lose!")
            return
        
        next_round = input("Type 'y' to get another card, type 'n' to pass:\n")
        if next_round == "y":
            give_cards(cards, user_hand, 1)
        else:
            while sum(computer_hand) < 17:
                give_cards(cards, computer_hand, 1)
            print(f"Your final hand: {user_hand}, final score: {sum(user_hand)}")
            print(f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")
            if check_over_21(computer_hand) or sum(user_hand) > sum(computer_hand):
                print("You win!")
            elif sum(user_hand) < sum(computer_hand):
                print("You lose!")
            else:
                print("It's a draw!")
            return

def main():
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n") == 'y':
        current_round()

main()
