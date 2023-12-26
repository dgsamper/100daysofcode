print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|    
      
''')
print("Welcome to the treasure island game!")
print("Your mission is to find the treasure!")
print("Let's begin!!")

first_step = input("Left or right?\n").lower()
if first_step == "left":
    second_step = input("Swim or wait?\n").lower()
    if second_step == "wait":
        third_step = input("Which door? Red, Blue or Yellow?\n").lower()
        if third_step == "yellow":
            print("You found the treasure. You won!")
        else:
            print("Game over.")    
    else:
        print("Game over")    
else:
    print("Game over")
