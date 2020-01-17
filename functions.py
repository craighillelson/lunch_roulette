""" __doc__ """

from collections import namedtuple
import csv

RTN = lambda: '\n'

def open_csv(a):
    with open('employees_and_executives.csv') as csv_file:
        F_CSV = csv.reader(csv_file)
        COLUMN_HEADINGS = next(F_CSV)
        CSV_ROW = namedtuple('Row', COLUMN_HEADINGS)
        for rows in F_CSV:
            row = CSV_ROW(*rows)
            a[row.email] = row.level


def append_list(a, b, c, d):
    """ adds selections to a list """
    for a in b:
        c.append(d[a])


def write_to_csv(output_csv, output_lst):
    """ write results to csv, print same, and print a return for readability """
    with open(output_csv, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(['email'])
        for employee_email in output_lst:
            out_csv.writerow([employee_email])

def output_selections(a, b):
    print(a)
    for employee in b:
        print(employee)

    print(RTN())


def update_user(results):
    """ update user """
    print(f'{results} exported successfully')
