"""Add employees to 'employees_and_executives.csv'."""

import csv
import functions
import pyinputplus as pyip
from datetime import date
from collections import namedtuple

EMPLOYEES_AND_EXECUTIVES = {}
EMPLOYEES_TO_ADD = {}

today = date.today()

EMPLOYEES_AND_EXECUTIVES = functions.open_csv('employees_and_executives.csv')

print('\nemployees and executives')
for employee, level in sorted(EMPLOYEES_AND_EXECUTIVES.items()):
    print(employee, level)

domain = input('\nWhat is your domain name?\n> ')

while True:
    print('\nEnter the employee\'s name (or \'return\' to stop.):')
    email_prefix = input('> ')
    if email_prefix == '':
        break
    email = email_prefix + '@' + domain
    exec = pyip.inputYesNo('Is the employee an executive (yes/no)?\n> ')
    if exec == 'yes':
        level = 'executive'
    else:
        level = 'employee'
    EMPLOYEES_AND_EXECUTIVES[email] = level
    EMPLOYEES_TO_ADD[email] = level

EMPLOYEES_AND_EXECUTIVES[email] = level

functions.write_dct_to_csv(EMPLOYEES_AND_EXECUTIVES)

for email, level in EMPLOYEES_TO_ADD.items():
    print('employee added')
    print(f'key: {email}')
    print(f'value: {level}')

print(functions.RTN())
