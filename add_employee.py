""" __doc__ """

# imports
import csv
from datetime import date
from collections import namedtuple

# functions and lambdas
RTN = lambda: '\n'

# data stores
EMPLOYEES_AND_EXECUTIVES = {}

# variables
today = date.today()

# open csv and populate EMPLOYEES_AND_EXECUTIVES with its contents
functions.open_csv(EMPLOYEES_AND_EXECUTIVES)

for employee, level in EMPLOYEES_AND_EXECUTIVES.items():
    print(employee, level)

# prompt user
domain = input('What is your domain name?\n')
email_prefix = input('Enter the email prefix of the employee to be added\n')
exec = input('Is the employee an executive (y/n)?\n')
email = email_prefix + '@' + domain
# determine domain name from existing employees and
# prompt user re: whether or not to use that domain when adding next employee
# prompt user re: how many employees they'd like to add
# num_emp_to_add = int(input('How many employees would you like to add?\n'))

# assign level based on user response
if exec == 'y':
    level = 'executive'
else:
    level = 'employee'

# populate dictionary with user input
EMPLOYEES_AND_EXECUTIVES[email] = level

# write user input to 'employees_and_executives.csv'
HEADERS = 'employee', 'level'

with open('employees_and_executives.csv', 'w') as out_file:
    out_csv = csv.writer(out_file)
    out_csv.writerow(HEADERS)
    for email, level in EMPLOYEES_AND_EXECUTIVES.items():
        keys_values = (email, level)
        out_csv.writerow(keys_values)

# update user
print('employee added')
print(f'key: {email}')
print(f'value: {level}')
