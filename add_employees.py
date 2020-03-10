""" __doc__ """

# imports
import csv
import functions
from datetime import date
from collections import namedtuple

# data stores
EMPLOYEES_AND_EXECUTIVES = {}
EMPLOYEES_TO_ADD = {}

# variable
today = date.today()

# open csv and populate EMPLOYEES_AND_EXECUTIVES with its contents
EMPLOYEES_AND_EXECUTIVES = functions.open_csv('employees_and_executives.csv')

for employee, level in EMPLOYEES_AND_EXECUTIVES.items():
    print(employee, level)

print(functions.RTN())

domain = input('What is your domain name?\n')

# prompt user
while True:
    print('Enter the employee\'s name (or \'return\' to stop.):')
    email_prefix = input()
    if email_prefix == '':
        break
    email = email_prefix + '@' + domain
    exec = input('Is the employee an executive (y/n)?\n')
    if exec == 'y':
        level = 'executive'
    else:
        level = 'employee'
    EMPLOYEES_AND_EXECUTIVES[email] = level
    EMPLOYEES_TO_ADD[email] = level

# populate dictionary with user input
EMPLOYEES_AND_EXECUTIVES[email] = level

functions.write_dct_to_csv(EMPLOYEES_AND_EXECUTIVES)

# update user
for email, level in EMPLOYEES_TO_ADD.items():
    print('employee added')
    print(f'key: {email}')
    print(f'value: {level}')

print(functions.RTN())
