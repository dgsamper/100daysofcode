# nested lists


fruits = ["Apple", "Orange", "Melon", "Blueberry"]
vegetables = ["Potato", "Tomato", "Carrot"]


nested_list: list = [fruits,vegetables]

print(nested_list)
print(type(nested_list))


print(nested_list[0][0]) # first item of the first list