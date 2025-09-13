import csv
file = open("contacts.csv", "r")
reader = csv.reader(file)
for row in reader:
    print(row)
file.close()