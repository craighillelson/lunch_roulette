"""List employees."""

from functions import (open_csv_pop_dct_namedtuple,
                       output_employees_and_executives)

employees_and_executives = open_csv_pop_dct_namedtuple()
output_employees_and_executives(employees_and_executives)
