# Write your code below this line 👇

def prime_checker(number):
    prime_numbers = []
    
    for n in range(2,number):
        prime_numbers.append(6*n - 1)
        prime_numbers.append(6*n + 1)
    
    if number in prime_numbers:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)