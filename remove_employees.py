"""Remove employees from 'employees_and_executives.csv'."""

# import
import functions

# data stores
EMPLOYEES_AND_EXECUTIVES = {}
EMPLOYEES_AND_EXECUTIVES_UPDATED = {}

# populate dictonary and provide options to user
EMPLOYEES_AND_EXECUTIVES = functions.open_csv('employees_and_executives.csv')

for i, (email, level) in enumerate(EMPLOYEES_AND_EXECUTIVES.items(), 1):
    print(f'{i} {email} {level}')

print(functions.RTN())

# prompt user
del_emp = input('select an employee to remove from list\n')

for i, (email, level) in enumerate(EMPLOYEES_AND_EXECUTIVES.items(), 1):
    if del_emp != email:
        EMPLOYEES_AND_EXECUTIVES_UPDATED[email] = level
    else:
        pass

print(functions.RTN())

# update user
print('updated list')
for i, (email, level) in enumerate(EMPLOYEES_AND_EXECUTIVES_UPDATED.items(), 1):
    print(i, email, level)

functions.write_dct_to_csv(EMPLOYEES_AND_EXECUTIVES_UPDATED)

print(functions.RTN())

print('"employees_and_executives.csv" updated successfully')

print(functions.RTN())
