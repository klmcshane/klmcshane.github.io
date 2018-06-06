names = ["Draco Malfoy",
"Albus Potter",
"Scorpius Malfoy",
"Albus Dumbledore",
"Rose Weasley",
"Ron Weasley",
"Minerva McGonagall"]
age = []

years = [1980, 1980, 2009, 2008, 1802, 2009, 1980, 1899]

for year in years:
    age.append (2018 - year)

for name in names:
    print(name + " is " + str(age[0]) + " years old.")
