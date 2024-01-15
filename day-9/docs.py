dictionaries = {
    "Slatt": "🐍",
    "Snare": "🥁",
    "Vampire": "🧛🏻"
}


print(dictionaries["Slatt"])  # prints the value of an item

dictionaries["Smile"] = "😀" # adds or edit an item
print(dictionaries)

# loop thru a dict

for key in dictionaries:
    print(key) # only prints the key
    print(dictionaries[key]) # only prints the value)



# Nesting
    
countries = {
    "Europe": {"countries_visited": ["France", "Spain", "Estonia", "Switzerland"], "total_visits": 77},
    "North America": {"countries_visited": ["USA", "Canada"]}
}


list_of_countries = [
    {"Europe": {"countries_visited": ["France", "Spain", "Estonia", "Switzerland"], "total_visits": 77}},
    {"North America": {"countries_visited": ["USA", "Canada"]}}
]

print(list_of_countries[0]) # "Europe"




dict = [
    {"Key":"Value", "Key2":"Value2"},
    {"Key3": ["Value3", "Value4"], 1: [1,2,3,4,5]}
]

print(dict[1]["Key3"][0]) # Value3