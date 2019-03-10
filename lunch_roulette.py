""" __doc__ """

import random

EMPLOYEES_AND_EXECUTIVES = {
    "michael@dundermifflin.com": "executive",
    "jim@dundermifflin.com": "employee",
    "pam@dundermifflin.com": "employee",
    "kevin@dundermifflin.com": "employee",
    }

EXECUTIVES = []
EMPLOYEES = []

for k, v in EMPLOYEES_AND_EXECUTIVES.items():
    if v == "executive":
        EXECUTIVES.append(k)
    else:
        EMPLOYEES.append(k)

NUMBER_OF_GUESTS = int(input("How many guests would you like to invite? "))
print(NUMBER_OF_GUESTS)

random_numbers_lst = random.sample(range(0, len(EMPLOYEES)), NUMBER_OF_GUESTS)
