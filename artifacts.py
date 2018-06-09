import csv

# if we have a new line inside of a quoted section, we want to be able to diferentiate that from an actual new line marking a new line.
with open('museum.csv', newline = '') as csv:
    # in case a delimeter different from a comma is used
    # artreader = csv.reader(csvfile, delimeter='|')
    artreader = csv.Dictreader(csvfile, delimeter='|')
    rows = list(artreader)
    for row in rows[:2]:
        print(row['group1'])