import util as u

def caesar(text, shift, direction):
        message = ""
        if direction == "decode":
             shift *= -1
        for letter in text:
            if letter in u.alphabet:
                original_index = u.alphabet.index(letter)
                new_index = (original_index + shift) % len(u.alphabet)
                message += u.alphabet[new_index]
            else:
                message += letter

        print(f"The {direction}d text is {message}.")    

        

def main():
    print(u.logo)
    replay_boolean = True

    while replay_boolean:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(text=text,shift=shift,direction=direction)
        replay = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if replay == "no":
            replay_boolean = False
            print("Goodbye!")
        elif replay == "yes":
            continue
                     
main()

    

