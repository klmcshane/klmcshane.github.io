import csv
with open('basic.csv', 'r') as csvfile:
    our_reader = csv.reader(csvfile)
    names = [row for row in our_reader]

new_row = [2,'wayne','graham','meh']
names.append(new_row)
print(names)

a_row = [3,'fox','eliza','SO COOL']
names + a_row
