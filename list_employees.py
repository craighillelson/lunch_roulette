"""List employees."""

from functions import (open_csv_pop_dct_namedtuple,
                       output_employees_and_executives)

EMPLOYEES_AND_EXECUTIVES = open_csv_pop_dct_namedtuple()
if EMPLOYEES_AND_EXECUTIVES:
    output_employees_and_executives(EMPLOYEES_AND_EXECUTIVES)
else:
    print('\nno employees in database')
