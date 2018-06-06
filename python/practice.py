import csv
with open('practice.csv', 'w') as fout:
    csvwriter = csv.writer(fout)
    for i in range(0, 100, 10):
        csvwriter.writerow([i, i + 5, i + 10, i + 15, i + 20])

with open('csvs/practice.csv', 'r') as fin:
    our_reader = csv.reader(fin)
    data = [row for row in our_reader]

with open('csvs/practice.csv', 'w') as fout:
    csvwriter = csv.writer(fout)
    for row in data:
        csvwriter.writerow(row)

print(data)
