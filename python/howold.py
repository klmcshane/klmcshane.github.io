birth_dates = {"Harry Potter": 1980,
"Draco Malfoy": 1980,
"Albus Potter": 2009,
"Scorpius Malfoy": 2008,
"Albus Dumbledore": 1802,
"Rose Weasley": 2009,
"Ron Weasley": 1980,
"Minerva McGonagall": 1899}


nineteen_count = 0
twenty_count = 0
twentyone_count = 0

for name, year in birth_dates.items():
    if year < 1900:
        nineteen_count += 1
    elif year < 2000:
        twenty_count += 1
    else:
        twentyone_count += 1

print("There are " + str(nineteen_count) + " 19th c births, "
    + str(twenty_count) + " 20th c births, "
    + str(twentyone_count) + " 21st c births in my collection.")
