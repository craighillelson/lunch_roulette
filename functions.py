"""Functions."""

import pyinputplus as pyip

EMPLOYEES_CSV = 'csvs/employees_and_executives.csv'


def add_email_if_not_in_dct(str1, dct1, dct2, dct3, str2):
    """
    If email entered by user isn't already in the csv, add email to
    emails_to_add dictionary.
    """
    if str1 not in dct1.keys():
        dct2[str1] = dct3[str2]
    else:
        print('email already in csv')


def check_if_already_in_csv():
    """Check to see if what the user entered is already in the csv."""
    if email_address_to_add not in employees_and_executives.keys():
        emails_to_add[email_address_to_add] = LEVEL_MAP[level]
    else:
        print('email already in csv')


def concat_prefix_and_domain(str1, str2):
    """Concatenate email prefix, '@' symbol, and domain."""
    return str1 + '@' + str2


def not_a_weekend(user_specified_date):
    """Determine if the date entered is not a weekday."""
    import datetime

    day_index = user_specified_date.weekday()
    return day_index < 5


def open_csv_pop_dct_namedtuple():
    """Open a csv and populate a dictionary."""
    import csv
    from collections import namedtuple

    dct = {}

    with open(EMPLOYEES_CSV) as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple('Row', headings)
        for r in f_csv:
            row = Row(*r)
            dct[row.email] = row.level

    return dct


def output_employees_not_selected(lst1, lst2):
    """Print a list of employees not selected."""
    print('\nemployees not selected')
    for email in lst1:
        if email not in lst2:
            print(email)
        else:
            pass


def output_employees_and_executives(dct):
    """Print a list of all employees and executives."""
    print('\n')
    print('email,level')
    for email, level in dct.items():
        print(f'{email},{level}')


def prompt_user_for_email_prefix():
    """Prompt user for email prefix."""
    return pyip.inputStr('\nenter the user\'s email prefix or nothing to quit'
                         '\n> ', blank=True)


def prompt_user_for_number_guests_to_invite():
    """Prompt user for the number of guests they'd like to invite."""

    return pyip.inputInt('\nHow many guests would you like to invite?\n> ')


def remove_selected_employees(dct2, lst):
    """
    Remove selected employees from the master list of employees and executives.
    """
    dct1 = {}
    for email, level in dct2.items():
        if email not in lst:
            dct1[email] = level
        else:
            pass

    return dct1


def select_an_executive(lst):
    """Prompt user to select an executive."""
    print('\nPlease select an executive.')
    for num, executive in enumerate(lst, 1):
        print(num, executive)
    return pyip.inputMenu(lst, prompt='> ', blank=True, numbered=True)


def write_employees_to_csv(file, DCT):
    """Write dictionary to csv."""
    import csv

    with open(file, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(['email','level'])
        for email, level in DCT.items():
            keys_values = (email, level)
            out_csv.writerow(keys_values)

    print(f'\n"{file}" exported successfully')


def write_lst_to_csv(file, lst):
    """Write list to csv """
    import csv

    with open(file, 'w') as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(['guests'])
        for email in lst:
            out_csv.writerow([email])

        print(f'\n"{file}" exported successfully')
