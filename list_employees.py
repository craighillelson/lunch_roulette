"""List employees and executives."""

import functions

employees_and_executives = functions.open_csv_pop_dct_namedtuple()
functions.output_employees_and_executives(employees_and_executives)
