food = {"breakfast": "eggs and bacon",
"lunch": "sandwiches",
"dinner": "burgers and salad",
"snack": "popcorn and cookies"}

def menu(x, y):
    print ("For " + x + " we will be having " + y + ".")

for meal, item in food.items():
    menu(meal, item)

def cocktail(x, y):
    print("I would also like to have a " + x + " and " + y + ".")

drinks = {"gin": "tonic",
"rum": "coke",
"Parrot Bay" : "pineapple"}

for x, y in drinks.items():
    cocktail(x, y)

import datetime
readable = datetime.datetime.fromtimestamp(1528210783).isoformat()
print(readable)
