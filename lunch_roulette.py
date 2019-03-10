""" __doc__ """

EMPLOYEES_AND_EXECUTIVES = {
    "michael@dundermifflin.com": "executive",
    "jim@dundermifflin.com": "employee",
    "pam@dundermifflin.com": "employee",
    }

EXECUTIVES = []
EMPLOYEES = []

for k, v in EMPLOYEES_AND_EXECUTIVES.items():
    if v == "executive":
        EXECUTIVES.append(k)
    else:
        EMPLOYEES.append(k)

NUMBER_OF_GUESTS = input("How many guests would you like to invite? ")
print(NUMBER_OF_GUESTS)
