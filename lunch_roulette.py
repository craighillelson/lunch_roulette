""" __doc__ """

import csv
import random
from collections import namedtuple

RTN = lambda: '\n'

def output_selections(output_csv, output_lst, output_heading):
    """ write results to csv, print same, and print a return for readability """
    with open(output_csv, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(["email"])
        for employee_email in output_lst:
            out_csv.writerow([employee_email])

    print(output_heading)
    for employee_email in output_lst:
        print(employee_email)

    print(RTN())


def update_user(results):
    """ update user """
    print(f'{results} exported successfully')


EMPLOYEES_AND_EXECUTIVES = {}
EXECUTIVES = []
EMPLOYEES = []
GUESTS = []

with open('employees_and_executives.csv') as csv_file:
    F_CSV = csv.reader(csv_file)
    COLUMN_HEADINGS = next(F_CSV)
    CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
    for rows in F_CSV:
        row = CSV_ROW(*rows)
        EMPLOYEES_AND_EXECUTIVES[row.email] = row.level

for email, level in EMPLOYEES_AND_EXECUTIVES.items():
    if level == 'executive':
        EXECUTIVES.append(email)
    else:
        EMPLOYEES.append(email)

for executive in EXECUTIVES:
    executives_guests = executive[:executive.find('@')].upper()+'S_GUESTS'

while True:
    try:
        NUMBER_OF_GUESTS = int(input('How many guests would you '
                                     'like to invite? '))
        if NUMBER_OF_GUESTS > len(EMPLOYEES):
            print(f'please enter a number less than or equal to '
                  f'{len(EMPLOYEES)}')
        else:
            print(RTN())
            break
    except ValueError:
        print('Please enter an integer.')

RANDOM_NUMBERS_LST = random.sample(range(0, len(EMPLOYEES)),
                                   NUMBER_OF_GUESTS)

for employee in RANDOM_NUMBERS_LST:
    GUESTS.append(EMPLOYEES[employee])

NOT_SELECTED = [employee for employee in EMPLOYEES if employee not in GUESTS]

output_selections('guests.csv', GUESTS,
                  'The following employees were selected:')
output_selections('not_selected.csv', NOT_SELECTED,
                  'The following employees were not selected:')

update_user('guests.csv')
update_user('not_selected.csv')

print(RTN())
