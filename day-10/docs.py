def format_name(f_name, l_name):
    """Returns both arguments with a capital letter."""

    if f_name == "" or l_name == "":
        return # None in this case. Used to escape the function
    
    return f"{f_name.title()} {l_name.title()}"


formatted_name = format_name("WelleRsSon","CASTRO")
print(formatted_name)
    