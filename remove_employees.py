"""Remove employees from csv."""

import functions
from functions import EMPLOYEES_CSV

employees_and_executives = functions.open_csv_pop_dct_namedtuple()
list_of_employees = list(employees_and_executives.keys())

print('\nEmployees')
for num, email in enumerate(list_of_employees, 1):
    print(num, email)

employees_to_remove = []

while True:
    print('\nPlease select an employee to remove or nothing to quit.')
    selection = functions.pyip.inputMenu(list_of_employees, prompt='> ',
                                         blank=True, numbered=True)
    if selection != '':
        employees_to_remove.append(selection)
    else:
        break

updated_employees = functions.remove_selected_employees(
    employees_and_executives,
    employees_to_remove)

for email, level in updated_employees.items():
    print(email, level)

functions.write_employees_to_csv(EMPLOYEES_CSV, updated_employees)
