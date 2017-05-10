import re
import csv

match = '\wo\w'

with open("worklog.csv", "r") as file:
    data = csv.reader(file)
    next(data)
    for row in data:
        for field in row:
            if re.search(match, field):
                print(row)
