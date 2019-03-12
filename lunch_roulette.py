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
GUESTS = []

for email, level in EMPLOYEES_AND_EXECUTIVES.items():
    if level == "executive":
        EXECUTIVES.append(email)
    else:
        EMPLOYEES.append(email)

while True:
    try:
        NUMBER_OF_GUESTS = int(input("How many guests would you like "
                                     "to invite? "))
        if NUMBER_OF_GUESTS > len(EMPLOYEES):
            print(f"please enter a number less than or equal to "
                  f"{len(EMPLOYEES)}")
        else:
            break
    except ValueError:
        print("Please enter an integer.")

RANDOM_NUMBERS_LST = random.sample(range(0, len(EMPLOYEES)), NUMBER_OF_GUESTS)

for employee in RANDOM_NUMBERS_LST:
    GUESTS.append(EMPLOYEES[employee])

print("The following employees were selected:")
for employee in GUESTS:
    print(employee)
