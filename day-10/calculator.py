import util as u

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2



operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}



def main():
    print(u.logo)
    num1 = float(input("What's the first number?\n"))
    num2 = float(input("What's the second number?\n"))

    continue_boolean = True
    for operation in operations:
        print(operation)

    operation_symbol = input("Pick an operation from the line above:\n ")

    operation_function = operations[operation_symbol]
    answer = operation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    while continue_boolean:
        continue_calculation = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation, or 'exit' to exit.:\n")
        if continue_calculation == "y":
            operation_symbol = input("Pick another operation:\n")
            num3 = float(input("What's the next number?\n"))
            operation_function = operations[operation_symbol]
            new_answer = operation_function(answer, num3)

            print(f"{answer} {operation_symbol} {num3} = {new_answer}")
            answer = new_answer

        elif continue_calculation == "n":
            continue_boolean = False
            main()
        
        elif continue_calculation == "exit":
            break

main()















