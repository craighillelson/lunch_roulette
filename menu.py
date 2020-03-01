""" __doc__ """

import functions

options = {
    'a': 'add_employees.py',
    'b': 'lunch_roulette.py',
    'c': 'remove_employees.py',
}

def switch_case(a, b):
    """ switch case statement """
    options
    return options.get(b, 'nothing')

print(functions.RTN())

print('please select an option below')
print('a - add employees')
print('b - build a lunch guest list')
print('c - remove employees')

while True:
    usr_choice = input()
    functions.open_file(switch_case(options, usr_choice))
    break
