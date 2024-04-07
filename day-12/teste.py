fruits = 3

def add_fruits():
    global fruits # keyword to use edti the global variable
    fruits += 2 

add_fruits()
print(fruits)

# a better way is to return the variable 

def return_fruits():    
    return fruits + 2

fruits = return_fruits()
print(fruits)

# constants

URL = "http://"
TWITTER_HANDLE = "@slatt"