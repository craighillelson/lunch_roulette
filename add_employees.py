"""Add employees to csv."""

import functions
import pyinputplus as pyip
import random

employees_and_executives = functions.open_csv_pop_dct_namedtuple()
emails_to_add = {}

LEVEL_MAP = {
    'yes': 'executive',
    'no': 'employee',
    }

while True:
    print('\nenter an eamil address or enter nothing to quit')
    email = pyip.inputEmail('> ', blank=True)
    if email == '':
        break

    if email not in employees_and_executives.keys():
        level = functions.pyip.inputYesNo('is this employee an executive?\n> ')
        emails_to_add[email] = LEVEL_MAP[level]
    else:
        print('email already in csv')

employees_and_executives_updated = {**employees_and_executives, **emails_to_add}
print('\n')
for email, level in  employees_and_executives_updated.items():
    print(email, level)

functions.write_employees_to_csv(functions.EMPLOYEES_CSV,
                                 employees_and_executives_updated)
