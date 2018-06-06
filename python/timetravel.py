year = [800, 2020, 1410, 1902]

def greetings(y):
        if y <= 1450:
            print ("Hwaet!")
        elif y < 1950:
            print ("Hello!")
        else:
            print("Hey there.")
for y in year:
    greetings(y)
