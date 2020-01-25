""" __doc__ """

# import
import functions

# data stores
EMPLOYEES_AND_EXECUTIVES = {}
EMPLOYEES_AND_EXECUTIVES_UPDATED = {}

functions.open_csv('employees_and_executives.csv', EMPLOYEES_AND_EXECUTIVES)

for i, (employee, level) in enumerate(EMPLOYEES_AND_EXECUTIVES.items(), 1):
    print(f'{i} {employee} {level}')

print(functions.RTN())

# prompt user
del_emp = input('select an employee to remove from list\n')

for i, (employee, level) in enumerate(EMPLOYEES_AND_EXECUTIVES.items(), 1):
    if del_emp != employee:
        print(f'{i} {employee} {level}')
        EMPLOYEES_AND_EXECUTIVES_UPDATED[employee] = level
    else:
        pass

print(functions.RTN())

# update user
print('updated list')
for employee, level in EMPLOYEES_AND_EXECUTIVES_UPDATED.items():
    print(employee, level)

functions.write_dct_to_csv(EMPLOYEES_AND_EXECUTIVES_UPDATED)

print(functions.RTN())

print('"employees_and_executives.csv" updated successfully')

print(functions.RTN())
