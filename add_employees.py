"""Add employees to csv."""

import functions
import pyinputplus as pyip
import random

employees_and_executives = functions.open_csv_pop_dct_namedtuple()

emails_to_add = {}
while True:
    print('\nenter an eamil address or enter nothing to quit')
    email = pyip.inputEmail('> ', blank=True)
    if email != '':
        if email not in employees_and_executives.keys():
            level = pyip.inputYesNo('is this employee an executive?\n> ')
            if level != 'yes':
                level = 'employee'
            else:
                level = 'executive'
            emails_to_add[email] = level
        else:
            print('email already in csv')
    else:
        break

employees_and_executives_updated = {**employees_and_executives, **emails_to_add}
print('\n')
for email, level in  employees_and_executives_updated.items():
    print(email, level)

functions.write_employees_to_csv(functions.EMPLOYEES_CSV,
                                 employees_and_executives_updated)
