"""Remove employees from csv."""

import pyinputplus as pyip
from functions import (open_csv_pop_dct_namedtuple,
                       remove_selected_employees,
                       EMPLOYEES_CSV,
                       write_employees_to_csv)

EMPLOYEES_AND_EXECUTIVES = open_csv_pop_dct_namedtuple()
LIST_OF_EMPLOYEES = list(EMPLOYEES_AND_EXECUTIVES.keys())

print('\nEmployees')
for num, email in enumerate(LIST_OF_EMPLOYEES, 1):
    print(num, email)

EMPLOYEES_TO_REMOVE = []

while True:
    print('\nPlease select an employee to remove or nothing to quit.')
    SELECTION = pyip.inputMenu(LIST_OF_EMPLOYEES, prompt='> ',
                               blank=True, numbered=True)
    if SELECTION != '':
        EMPLOYEES_TO_REMOVE.append(SELECTION)
    else:
        break

UPDATED_EMPLOYEES = remove_selected_employees(EMPLOYEES_AND_EXECUTIVES,
                                              EMPLOYEES_TO_REMOVE)

for email, level in UPDATED_EMPLOYEES.items():
    print(email, level)

write_employees_to_csv(EMPLOYEES_CSV, UPDATED_EMPLOYEES)
