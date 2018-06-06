food = {"breakfast": "eggs and bacon",
"lunch": "sandwiches",
"dinner": "burgers and salad",
"snack": "popcorn and cookies"}

def menu(x, y):
    print ("For " + x + " we will be having " + y + ".")

for meal, item in food.items():
    menu(meal, item)
