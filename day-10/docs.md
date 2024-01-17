***DAY 10 - 15/01/2024 e 16/01/2024***

- Functions with output --> return keyword

def function():
    return 3*2

multiplication = function()  --> I can assign functions with output to variables

- docstrings -> just add """ """ to the first line of a function to create a docstring. It will appears in the popup when hovering in the function

def function(a, b):
    """Returns the multiplication of two numbers."""
    return a*b

To store functions in dictionaries ->

dict = {
    "key": function,
    "key2": function2
}