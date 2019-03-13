""" __doc__ """

import csv
import random
from collections import namedtuple

EMPLOYEES_AND_EXECUTIVES = {}
EXECUTIVES = []
EMPLOYEES = []
GUESTS = []

with open("employees_and_executives.csv") as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        EMPLOYEES_AND_EXECUTIVES[row.email] = row.level

for email, level in EMPLOYEES_AND_EXECUTIVES.items():
    if level == "executive":
        EXECUTIVES.append(email)
    else:
        EMPLOYEES.append(email)

for executive in EXECUTIVES:
    executives_guests = executive.upper()+"s_guests".upper()

while True:
    try:
        NUMBER_OF_GUESTS = int(input("How many guests would you "
                                     "like to invite? "))
        if NUMBER_OF_GUESTS > len(EMPLOYEES):
            print(f"please enter a number less than or equal to "
                  f"{len(EMPLOYEES)}")
        else:
            break
    except ValueError:
        print("Please enter an integer.")

RANDOM_NUMBERS_LST = random.sample(range(0, len(EMPLOYEES)),
                                   NUMBER_OF_GUESTS)

for employee in RANDOM_NUMBERS_LST:
    GUESTS.append(EMPLOYEES[employee])

with open("guests.csv", "w") as out_file:
    OUT_CSV = csv.writer(out_file)
    OUT_CSV.writerow(["guest_email"])
    for guest in GUESTS:
        OUT_CSV.writerow([guest])

print("The following employees were selected:")
for employee in GUESTS:
    print(employee)
