"""Provide user with a list of options and prompt them to make a selection."""

# import pyinputplus as pyip
import functions

choices = [
    'add_employees.py',
    'list_employees.py',
    'lunch_roulette.py',
    'remove_employees.py',
    'quit',
    ]

while True:
    print('\nPlease select from the options below.')
    for num, choice in enumerate(choices, 1):
        print(num, choice)
    selection = functions.pyip.inputMenu(choices, prompt='> ', blank=True,
                                         numbered=True)
    if selection != 'quit':
        exec(open(selection).read())
    else:
        break
