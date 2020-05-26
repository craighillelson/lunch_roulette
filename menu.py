"""Provide a list of options to the user."""

import functions

options = {
    'a': 'add_employees.py',
    'b': 'list_employees.py',
    'c': 'lunch_roulette.py',
    'd': 'remove_employees.py',
}

def switch_case(a, b):
    """Switch case statement."""
    options
    return options.get(b, 'nothing')

print(functions.RTN())

print('please select an option below')
print('a - add employees')
print('b - list employees')
print('c - build a lunch guest list')
print('d - remove employees')

while True:
    usr_choice = input('> ')
    functions.open_file(switch_case(options, usr_choice))
    break
