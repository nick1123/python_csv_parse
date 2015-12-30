import csv

people = {}

with open('peeps.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(csvreader) # Skip the first line
    for row in csvreader:
        print ', '.join(row)
