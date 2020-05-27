"""List employees and executives."""

import functions


def list_emps(a):
    """Output employees and executives."""
    functions.print_return()
    print('employees and executives')
    for employee, level in sorted(a.items()):
        print(f'{employee}, {level}')
    functions.print_return()


EMPLOYEES_AND_EXECUTIVES = functions.open_csv('employees_and_executives.csv')
list_emps(EMPLOYEES_AND_EXECUTIVES)
