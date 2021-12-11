"""Script to help user pair executives and employees for lunch"""

import csv
import os
import random
from datetime import date
import pyinputplus as pyip


def assign_level():
    return pyip.inputYesNo("is this employee an executive (yes or no): ")


def avoid_duplicate_email_addresses():
    email_addresses = build_list_of_email_addresses()
    while True:
        email_address = pyip.inputEmail("\nemail address: ", blank=True)
        if email_address in email_addresses:
            print("duplicate email address")
        else:
            return email_address


def build_list_of_email_addresses():
    contacts = import_csv()
    return contacts.keys()


def build_lists_of_employees_and_executives():
    contacts = import_csv()
    lst1 = []
    lst2 = []
    for email, level in contacts.items():
        if level == "yes":
            lst1.append(email)
        else:
            lst2.append(email)

    return lst1, lst2


def build_updated_dictionary(dct2):
    dct1 = {}
    for email_and_level in dct2.values():
        email = email_and_level[0]
        level = email_and_level[1]
        dct1[email] = level

    return dct1


def capture_attributes(dct1, dct2):
    while True:
        email = avoid_duplicate_email_addresses()
        if email == "":
            break

        level = assign_level()
        dct2[email] = level
        all_contacts = {**dct1, **dct2}

        write_dictionary_to_csv(all_contacts)

        add_another = pyip.inputYesNo("\nWould you like to add another "
                                      "(yes/no)? ")

        if add_another != "yes":
            break


def edit_email(email_address, lst):
    print("\nupdate value or enter nothing to keep current value")
    while True:
        print(f"\ncurrent email: {email_address}")
        edited_email = pyip.inputEmail("> ", blank=True)
        if edited_email in lst:
            print("duplicate email address")
        elif edited_email == "":
            edited_email = email_address
            break
        else:
            break

    return edited_email


def enumerate_contacts(dct1):
    dct2 = {}
    for number, (email, level) in enumerate(dct1.items(), 1):
        dct2[number] = [email, level]

    return dct2


def enumerate_list(lst):
    dct = {}
    for i, contact in enumerate(lst, 1):
        dct[i] = contact

    return dct


def import_csv():
    dct = {}
    with open("contacts.csv") as csv_file:
        imported_csv = csv.DictReader(csv_file)
        for row in imported_csv:
            dct[row["email"]] = row["executive"]

    return dct


def not_a_weekend(user_specified_date):
    day_index = user_specified_date.weekday()
    return day_index < 5


def output_added_contacts(header, dct):
    print(header)
    for email_address in dct.keys():
        print(email_address)


def output_contacts(dct):
    for number, (email, level) in dct.items():
        print(f"{number}. {email}, {level}")


def output_enumerated_executives(lst):
    executives_count = len(lst)
    enumerated_lst = enumerate_list(lst)
    if lst:
        if executives_count > 1:
            print("\nplease select an executive to host a lunch date")
            for number, email in enumerated_lst.items():
                print(f"{number}. {email}")
        else:
            print("\nexecutive")
            print(*lst)
    else:
        print("no executives found")

    return executives_count, enumerated_lst


def output_guest_list(host, lunch_date, lst1, lst2):
    print(f"\nguest list for lunch with {host} on {lunch_date}")
    for i in lst1:
        print(lst2[i])


def output_updated_contacts(dct):
    print("\nupdated contacts")
    for email, level in dct.items():
        print(email, level)


def populate_dictionary(dct2):
    dct1 = {}
    for email_address, level in dct2.values():
        dct1[email_address] = level

    return dct1


def prompt_user_for_number_of_guests(lst):
    print("\nHow many guests would you like to invite?")
    return pyip.inputInt("> ", min=1, max=len(lst))


def prompt_user_to_add_contacts():
    print("\nThe contacts list is empty. Let's add some contacts.")
    add_contacts()
    

def prompt_user_to_confirm_deletion(contact, dct, choice):
    print(f"\ndelete {contact} (yes or no)?")
    confirm_delete = pyip.inputYesNo("> ")
    if confirm_delete == "yes":
        del dct[choice]
        print("\nthe following contact was deleted")
        print(contact)


def prompt_user_to_select_an_executive(executives_count, dct):
    user_choice = pyip.inputInt("> ", min=1, max=executives_count)
    return dct[user_choice]


def prompt_user_to_update_level(contact, level1):
    print(f"would you like to update {contact}'s level?")
    update_level = pyip.inputYesNo("> ")
    if update_level == "yes":
        if level1 == "yes":
            level2 = "no"
        else:
            level2 = "yes"
    else:
        level2 = level1

    return level2


def write_dictionary_to_csv(dct):
    with open("contacts.csv", "w") as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(["email","executive"])
        for email, level in dct.items():
            keys_values = (email, level)
            out_csv.writerow(keys_values)


def create_contacts_csv_if_one_does_not_exist():
    if os.path.exists("contacts.csv"):
        pass
    else:
        open("contacts.csv", "w")


def test_for_four_employees_and_one_executive():
    while True:
        executives, employees = build_lists_of_employees_and_executives()
        number_of_executives = len(executives)
        number_of_employees = len(employees)
        if number_of_employees < 4:
            difference = 4 - number_of_employees
            print(f"\nyou need {difference} more employees before you can play "
                  f"lunch roulette")
            add_contacts()
        elif number_of_executives < 1:
            print("\nyou need at least one executive to play lunch roulette")
            print("\nwould you like to \n1. add an executive or\n"
                  "2. edit an employee record?")
            add_or_edit_menu = {
                1: "add",
                2: "edit"
            }
            user_choice = pyip.inputInt("> ", min=1, max=2)
            if add_or_edit_menu[user_choice] == "add":
                add_contacts()
            else:
                edit_contacts()
        else:
            break


def prompt_user_to_select_an_option():
    options_map = {
        1: ["add contacts", add_contacts],
        2: ["delete contacts", delete_contacts],
        3: ["edit contacts", edit_contacts],
        4: ["list contacts", list_contacts],
        5: ["build lunch schedule", build_lunch_schedule],
    }


    while True:
        print("\nselect an option below")
        for number, option in options_map.items():
            print(f"{number}. {option[0]}")
        user_choice = pyip.inputInt("> ", blank=True)
        if user_choice in list(options_map.keys()):
            options_map[user_choice][1]()
        elif user_choice not in list(options_map.keys()) and user_choice != "":
            print("\ninvalid choice")
        else:
            print("\nsession complete\n")
            break


def add_contacts():
    print("\n> add contact")
    contacts = import_csv()
    contacts_to_add = {}
    capture_attributes(contacts, contacts_to_add)

    if not contacts_to_add:
        pass
    elif len(contacts_to_add) > 1:
        output_added_contacts("\nthe following contacts were added",
                              contacts_to_add)
    else:
        output_added_contacts("\nthe following contact was added",
                              contacts_to_add)


def edit_contacts():
    print("\n> edit contact")

    while True:
        contacts = import_csv()
        if not contacts:
            prompt_user_to_add_contacts()
            break

        print("\nselect a contact to edit or enter nothing to exit")
        email_addresses = build_list_of_email_addresses()
        enumerated_contacts = enumerate_contacts(contacts)
        output_contacts(enumerated_contacts)
        number_of_contacts = len(enumerated_contacts)
        select_contact = pyip.inputInt("> ", min=1, max=number_of_contacts,
                                       blank=True)
        if select_contact == "":
            break

        selected_contact_attributes = enumerated_contacts[select_contact]

        email = selected_contact_attributes[0]
        level = selected_contact_attributes[1]

        updated_email = edit_email(email, email_addresses)
        updated_level = prompt_user_to_update_level(updated_email, level)
        enumerated_contacts[select_contact] = [updated_email, updated_level]
        updated_contacts = build_updated_dictionary(enumerated_contacts)
        write_dictionary_to_csv(updated_contacts)
        output_updated_contacts(updated_contacts)
        edit_another = pyip.inputYesNo("\nWould you like to edit another "
                                       "(yes/no)? ")

        if edit_another != "yes":
            break


def list_contacts():
    print("\n> list contacts")
    contacts = import_csv()
    if contacts:
        print("\nemail, executive")
        for email, level in sorted(contacts.items()):
            print(f"{email}, {level}")
    else:
        prompt_user_to_add_contacts()


def delete_contacts():
    print("\n> delete contacts")
    while True:
        print("\nselect a contact to delete or enter nothing to exit")
        contacts = import_csv()
        enumerated_contacts = enumerate_contacts(contacts)
        for number, (email_address, level) in enumerated_contacts.items():
            print(f"{number}. {email_address}, {level}")
        number_of_contacts = len(enumerated_contacts)
        user_choice = pyip.inputInt("> ", min=1, max=number_of_contacts,
                                    blank=True)

        if user_choice == "":
            break

        selected_contact = enumerated_contacts[user_choice][0]
        print(f"\nyou selected {selected_contact}")

        prompt_user_to_confirm_deletion(selected_contact, enumerated_contacts,
                                        user_choice)
        updated_contacts = {}
        updated_contacts = populate_dictionary(enumerated_contacts)
        write_dictionary_to_csv(updated_contacts)

        print("\nwould you like to delete another (yes or no)?")
        delete_another = pyip.inputYesNo("> ")
        if delete_another == "no":
            break


def build_lunch_schedule():
    test_for_four_employees_and_one_executive()
    print("\n> build lunch schedule")

    while True:
        today = date.today()
        selected_date = pyip.inputDate(prompt="\nPlease enter a date for lunch "
                                       "in 'YYYY-MM-DD' format\n> ",
                                       formats=["%Y-%m-%d"])
        if selected_date <= today:
            print("Please select a date in the future")
        elif not not_a_weekend(selected_date):
            print("Please select a date that doesn't fall on a weekend.")
        else:
            break

    executives, employees = build_lists_of_employees_and_executives()
    number_of_executives, enumerated_executives = \
    output_enumerated_executives(executives)
    if number_of_executives > 1:
        selected_executive = \
        prompt_user_to_select_an_executive(number_of_executives,
                                           enumerated_executives)
    else:
        pass

    number_of_guests = prompt_user_for_number_of_guests(employees)
    number_of_employees = len(employees)
    randomlist = random.sample(range(0, number_of_employees), number_of_guests)
    output_guest_list(selected_executive, selected_date, randomlist, employees)


create_contacts_csv_if_one_does_not_exist()
test_for_four_employees_and_one_executive()
prompt_user_to_select_an_option()
