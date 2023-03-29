"""Shop program"""
import sys


stock = {'charger': 11, 'kettle': 25,
         'headphones': 75, 'stereo': 140, 'robot': 99.50}
separator = "\n---------------------------------\n"
purchase_confirmation = "Congratulations on your purchase. Here’s your item: "
thank_you_mssg = f"\nThank you for visiting our shop! Goodbye.{separator}\n"


### Custom errors
class BudgetTooLow(ValueError):
    """Raise when user tries to purches item more than 3 times."""


class TooManyAttempts(Exception):
    """Raise error when attempts are higher than 3"""


### Setup
def print_welcome():
    """Print welcome header"""
    print('#' * 40)
    print('#', ' ' * 36, '#')
    print('#', ' ' * 7, "WELCOME TO OUR SHOP!", ' ' * 7, '#')
    print('#', ' ' * 36, '#')
    print('#' * 40)
    print("\nWhat we currently have in stock: \n")


def setup(items):
    """Print welcome and display times in the shop"""
    print_welcome()
    # print table headers
    print("Opt. |".rjust(4) + "Item".ljust(12) + "| Price")
    print("-" * 5 + "|" + "-" * 12 + "|" + "-" * 8)
    # go over items and add them to a list along with their option to use in user input
    item_list = []
    for i, (name, price) in enumerate(items.items(), 1):
        item_list.append({name: price})
        print(f"{i:>4} | {name.capitalize():<10} | {price:.2f}")
    item_list.append("Exit shop?")
    print("-" * 27)
    print(f"{len(item_list):>4} | Exit shop? \n")
    print(f"To EXIT the shop, select the last option ({len(item_list)}).")
    return item_list


### Validation functions
def validate_confirmation(user_input):
    """Check if y/n confirmation is valid and exit if n"""
    if user_input not in ['y', 'n']:
        raise ValueError("  Invalid input. Please type in 'y' or 'n'.\n")
    if user_input == 'n':
        sys.exit()


def validate_budget(budget, price):
    """Check if budget is higher than the price"""
    if budget < price:
        raise BudgetTooLow("    You do not have enough money to buy this item.\n")


def validate_attempts(attempt):
    """Check number of attempts"""
    if attempt >= 3:
        raise TooManyAttempts("---Too many unsuccessful attempts. Try again later.---\n")


def validate_user_selection(user_input, item_list):
    """Validate user input and return the selected item"""
    if not user_input:
        raise ValueError("  You did not type anything.")

    if not user_input.isdigit() or int(user_input) < 1 or int(user_input) > len(item_list):
        raise ValueError(f"""   Invalid input. Please select item \
between 1 and {len(item_list)-1} or {len(item_list)} to exit.""")
    index = int(user_input) - 1
    return item_list[index]


def validate_extra_budget_input(user_input):
    """Validate user input and return the selected item"""
    if not user_input:
        raise ValueError("\n  You did not type anything.")

    if user_input.isalpha() or user_input.isalnum() and not user_input.isdigit():
        raise ValueError("\n  Invalid input. Your selection must be a number.")
    if int(user_input) < 1:
        raise ValueError("\n  Invalid input. Your selection must be greater than 0.")


### Main functions
def make_selection(item_list):
    """Ask user to select the item"""
    while True:
        option = input(
            "From the table above select the \
number matching the item you want to buy: ")
        print(separator)
        try:
            selection = validate_user_selection(option, item_list)
        except ValueError as error:
            print(f"{error} Try again.\n")
            continue
        else:
            option = int(option)
            check_if_exit(option, item_list)
            selection = item_list[option-1]
        return selection


def check_if_exit(option, item_list):
    """Exit program if selection is Exit"""
    if option == len(item_list):
        print(thank_you_mssg)
        sys.exit()

def check_budget(selection):
    """Check if user's purchase is within budget"""
    customer_budget = 100
    attempt = 1
    for k, v in selection.items():
        item = k
        price = v
    try:
        validate_budget(customer_budget, price)

    except BudgetTooLow as error:
        print(error)
        while True:
            try:
                validate_attempts(attempt)
                increase_budget = input(
                    "Do you want increase your budget? y/n ").lower()
                validate_confirmation(increase_budget)
                while True:
                    try:
                        extra_budget = input(
                            "\nPlease type by how much more you can spend: ")
                        validate_extra_budget_input(extra_budget)
                    except ValueError as v_error:
                        print(v_error)
                        continue
                    else:
                        break
                attempt += 1
                customer_budget += int(extra_budget)
                print(f"\nYou inreased your budget to £{customer_budget}")
                validate_budget(customer_budget, price)
                print(f"{separator}{purchase_confirmation} \n\n {item.upper()} - £{price}")
                break
            except ValueError as v_error:
                print(f"\n{v_error}")
            except TooManyAttempts as c_error:
                print(f"\n{c_error}")
                break
    else:
        print(
            f"{purchase_confirmation} \n\n {item.upper()} - £{price}")
    finally:
        print(thank_you_mssg)
        sys.exit()


def run_shop():
    """Run shop program"""
    options = setup(stock)
    selection = make_selection(options)
    check_budget(selection)


if __name__ == '__main__':
    run_shop()
