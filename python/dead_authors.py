author_death = {"Charles Dickens": "1870",
"William Thackeray": "1863",
"Anthony Trollope": "1882",
"Gerard Manley Hopkins": "1889",
"Geoffrey Chaucer": "1400",
"John Gower": "1408"}

def deadguys(x, y):
    print(x + " kicked the bucket in " + y + ".")

for author, year in author_death.items():
    deadguys(author, year)

def greetings(x,y):
    if int(y)<=1450:
        print("Hwaet, " + x + "!")
    elif int(y)<=1880:
        print("Why hello there, " + x + "!")
    else:
        print("Good morning, " + x + ".")

for x, y in author_death.items():
    greetings (x, y)
