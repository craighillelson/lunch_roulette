"""Add employees to csv."""

import pyinputplus as pyip
from functions import (open_csv_pop_dct_namedtuple,
                       prompt_user_for_email_prefix,
                       concat_prefix_and_domain,
                       add_email_if_not_in_dct,
                       write_employees_to_csv,
                       EMPLOYEES_CSV)

employees_and_executives = open_csv_pop_dct_namedtuple()

LEVEL_MAP = {
    "yes": "executive",
    "no": "employee",
    }

email_addresses = list(employees_and_executives.keys())
domain = email_addresses[0].split('@')[1]
domain_answer = pyip.inputYesNo(f"\nIs {domain} the domain name for users "
                                f"you'd like to add?\n> ")
emails_to_add = {}

if domain_answer != "yes":
    domain = pyip.inputStr("Please enter the domain name associated with the "
                           "users you'd like to add\n> ")
else:
    pass

while True:
    email_prefix = prompt_user_for_email_prefix()
    if email_prefix == "":
        break

    email_address_to_add = concat_prefix_and_domain(email_prefix, domain)
    level = pyip.inputYesNo("is this employee an executive?\n> ")
    add_email_if_not_in_dct(email_address_to_add,
                            employees_and_executives,
                            emails_to_add,
                            LEVEL_MAP, level)

employees_and_executives_updated = {**employees_and_executives, **emails_to_add}
print("\n")
for email, level in  employees_and_executives_updated.items():
    print(email, level)

write_employees_to_csv(EMPLOYEES_CSV, employees_and_executives_updated)
