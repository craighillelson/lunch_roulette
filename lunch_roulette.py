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

for email, level in EMPLOYEES_AND_EXECUTIVES.items():
    if level == "executive":
        EXECUTIVES.append(email)
    else:
        EMPLOYEES.append(email)

NUMBER_OF_GUESTS = int(input("How many guests would you like to invite? "))
print(NUMBER_OF_GUESTS)

RANDOM_NUMBERS_LST = random.sample(range(0, len(EMPLOYEES)), NUMBER_OF_GUESTS)
