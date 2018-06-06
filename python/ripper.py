import csv

with open('csvs/ripper.csv', 'r') as fin:
    reader = csv.reader(fin)
    results = [row for row in reader]

for row in results:
    row[4] = row[4].lower()

with open('ripper_texts.csv', 'w') as fout:
    writer = csv.writer(fout)
    for row in results:
        writer.writerow(row)
