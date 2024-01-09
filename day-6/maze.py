# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# Maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def find_right_wall():
    while front_is_clear():
        move()
    turn_left()
    

def main():
    find_right_wall()
    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()
    
        
                   
main()