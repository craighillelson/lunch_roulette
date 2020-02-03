""" __doc__ """

# imports
import csv
import functions
import random
from datetime import date
from datetime import datetime

# variables
TODAYS_DATE = date.today()

# data stores
EMPLOYEES_AND_EXECUTIVES = {}
EXECUTIVES = []
EMPLOYEES = []
GUESTS = []
HOST = []

# strip '@' and domain from email address
# for executive in EXECUTIVES:
#     executives_guests = executive[:executive.find('@')].upper()+'S_GUESTS'

# populate dictionary with staff members and their respective levels
functions.open_csv('employees_and_executives.csv', EMPLOYEES_AND_EXECUTIVES)

# separate users by into executives and employees
for email, level in EMPLOYEES_AND_EXECUTIVES.items():
    if level == 'executive':
        EXECUTIVES.append(email)
    else:
        EMPLOYEES.append(email)

# prompt user for number of guests
while True:
    try:
        NUMBER_OF_GUESTS = int(input('How many guests would you '
                                     'like to invite? '))
        if NUMBER_OF_GUESTS > len(EMPLOYEES):
            print(f'please enter a number less than or equal to '
                  f'{len(EMPLOYEES)}')
        else:
            print(functions.RTN())
            break
    except ValueError:
        print('Please enter an integer.')

# populate a list of random numbers equal in length the number specified by user
RANDOM_GUESTS = random.sample(range(0, len(EMPLOYEES)), NUMBER_OF_GUESTS)

# using the list of random numbers as indexes, populate a list of employees
functions.append_list('employee', RANDOM_GUESTS, GUESTS, EMPLOYEES)

NOT_SELECTED = [employee for employee in EMPLOYEES if employee not in GUESTS]

# populate a list that includes one random number
RANDOM_HOST = random.sample(range(0, len(EXECUTIVES)), 1)

# using the list of random number as an index,
# populate a list that includes one executive
for executive in RANDOM_HOST:
    exec_host = EXECUTIVES[executive]

# format date
TODAYS_DATE_FORMATTED = datetime.strftime(TODAYS_DATE, '%Y-%m-%d')

# concatonate strings
date_guests_csv = TODAYS_DATE_FORMATTED + '_guests.csv'
not_selected_csv = TODAYS_DATE_FORMATTED + '_not_selected.csv'

# write results to a csv
functions.write_list_to_csv(date_guests_csv, GUESTS) #,
functions.write_list_to_csv(not_selected_csv, NOT_SELECTED)

# update the user
functions.output_selections(f'The following employees were selected to be '
                            f'invited to lunch hosted by {exec_host}:', GUESTS)
functions.output_selections('The following employees were not selected:',
                            NOT_SELECTED)

# update user
functions.update_user(date_guests_csv)
functions.update_user(not_selected_csv)

print(functions.RTN())
