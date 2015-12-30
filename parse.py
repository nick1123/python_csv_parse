import csv
import pprint

pp = pprint.PrettyPrinter(indent=2)

people = {}

def parse_csv_1_row(row, people):
    person = {'first': row[1], 'last': row[2]}
    people[row[0]] = person

with open('peeps.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(csvreader) # Skip the first line because it's a header
    for row in csvreader:
        parse_csv_1_row(row, people)

pp.pprint(people)
