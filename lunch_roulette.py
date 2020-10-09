"""
Select executives and a number of random employees to go to lunch together.
"""

from datetime import date
import random
import functions

today = date.today()

while True:
    lunch_date = functions.pyip.inputDate(prompt="\nPlease enter a date for "
                                          "lunch in 'YYYY-MM-DD' format\n> ",
                                          formats=["%Y-%m-%d"])
    if lunch_date <= today:
        print("Please select a date in the future")
    elif not functions.not_a_weekend(lunch_date):
        print("Please select a date that doesn't fall on a weekend.")
    else:
        break

employeess_and_executives = functions.open_csv_pop_dct_namedtuple()

employees = []
executives = []
for email, level in employeess_and_executives.items():
    if level != "executive":
        employees.append(email)
    else:
        executives.append(email)

user_selected_executive = functions.select_an_executive(executives)

number_of_guests = functions.prompt_user_for_number_guests_to_invite()

random_guests = random.sample(range(0, len(employees)), number_of_guests)
print(f"\nsuggested lunch guests to join {user_selected_executive} on "
      f"{lunch_date}")

guests = []

for guest in random_guests:
    guests.append(employees[guest])

for num, email in enumerate(guests, 1):
    print(num, email)

functions.output_employees_not_selected(employees, guests)

GUEST_LIST = str(lunch_date) + "_" + str(user_selected_executive) + ".csv"
functions.write_lst_to_csv(GUEST_LIST, guests)
