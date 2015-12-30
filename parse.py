import csv
import pprint

def parse_csv_1_row(row, people):
    person = {'first': row[1], 'last': row[2]}
    people[row[0]] = person

def parse_csv_1(people):
    with open('peeps.csv', 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(csvreader) # Skip the first line because it's a header
        for row in csvreader:
            parse_csv_1_row(row, people)

def parse_csv_2_row(row, people):
    id = row[0]
    person = people[id]
    person['age'] = row[1]

def parse_csv_2(people):
    with open('peeps2.csv', 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(csvreader) # Skip the first line because it's a header
        for row in csvreader:
            parse_csv_2_row(row, people)


people = {}
parse_csv_1(people)
parse_csv_2(people)

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(people)
