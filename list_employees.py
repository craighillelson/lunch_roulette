""" __doc__ """

import functions

EMPLOYEES_AND_EXECUTIVES = functions.open_csv('employees_and_executives.csv')

print(functions.RTN())

print('employees and executives')
for employee, level in EMPLOYEES_AND_EXECUTIVES.items():
    print(f'{employee}, {level}')

print(functions.RTN())
