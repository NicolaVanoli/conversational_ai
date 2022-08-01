import csv

path = "transcriptions/database.csv"

#Read in Data
rows = []

with open(path, newline='') as csvfile:

    reader = csv.reader(csvfile)

    for row in reader:
        rows.append(row)
        print(row)

rows.append(['8','9','10'])

#Write the Data to File
with open(path, 'w', newline='') as csvfile:

   writer = csv.writer(csvfile)

   writer.writerows(rows)