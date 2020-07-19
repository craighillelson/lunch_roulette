"""Lunch roulette functions."""

import csv
import pyinputplus as pyip
from collections import namedtuple


RTN = lambda: '\n'

GUESTS = []


def print_return():
    """Print a return."""
    print('\n')


def open_csv(file):
    """Open a csv and populate a dictionary with its contents."""
    DCT = {}

    with open(file) as csv_file:
        F_CSV = csv.reader(csv_file)
        COLUMN_HEADINGS = next(F_CSV)
        CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
        for rows in F_CSV:
            row = CSV_ROW(*rows)
            DCT[row.email] = row.level

    return DCT


def append_list(a, b, c, d):
    """Add selections to a list."""
    for a in b:
        c.append(d[a])


def write_dct_to_csv(a):
    """Write dictionary to csv."""
    HEADERS = 'email','level'
    with open('employees_and_executives.csv', 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(HEADERS)
        for email, level in a.items():
            keys_values = (email, level)
            out_csv.writerow(keys_values)


def write_list_to_csv(output_csv, output_lst):
    """Write results to csv, print same, and print a return for readability."""
    with open(output_csv, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(['email'])
        for employee_email in output_lst:
            out_csv.writerow([employee_email])


def output_selected(a, b):
    """Print host and selected employees."""
    print('Host')
    print(a)
    print_return()
    print('Guests')
    for employee in b:
        print(employee)

    print_return()


def output_not_selected(a):
    """Print employees not selected."""
    print('The following employees were not selected:')
    for employee in a:
        print(employee)

    print_return()


def update_user(results):
    """Update user."""
    print(f'{results} exported successfully')


def open_file(a):
    """Open python script in response to user selection."""
    exec(open(a).read())
