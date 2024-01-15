import os
import util as u



def add_to_dict(key,value,dictionary):
    dictionary[key] = value

def highest_bid(dictionary):
    highest_bidder = max(dictionary, key=dictionary.get)
    highest_bid = dictionary[highest_bidder]
    
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}!")



def main():
    print(u.logo)
    print("Welcome to the secret auction program.")
    
    temp_dict = {}
    other_bidders = True
    while other_bidders:
        name = input("What's your name?\n")
        bid = int(input("What's your bid?\n$"))
        
        add_to_dict(name, bid, temp_dict)
        
        other_users = input("There are other users to bid? Type 'yes' or 'no':\n")
        
        if other_users == "yes":
            os.system("clear")
            continue
        elif other_users == "no":
            highest_bid(temp_dict)
            other_bidders = False

main()
