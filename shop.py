
"""Shop program"""

# Setup
stock = {'charger': 11, 'kettle': 25,
         'headphones': 75, 'stereo': 140, 'Robot': 99.50}
# A thank you message for the customer
thank_you_mssg = "Thank you for visiting our shop! Goodbye."

# Custom errors


class BudgetTooLow(ValueError):
    """Raise when user tries to purches item more than 3 times."""


class TooManyAttempts(Exception):
    """Raise error when attempts are higher than 3"""

# Welcome the customer and display the items and their prices, along with an option to “exit”


def setup(items):
    """Print welcome and display times in the shop"""
    print("Welcome to the shop!")
    print("What we have currently in stock: \n")
    # print table headers
    print("Opt. |".rjust(4) + "Item".ljust(12) + "| Price")
    print("-" * 5 + "|" + "-" * 12 + "|" + "-" * 8)
    # go over items and add them to a list along with their option to use in user input
    item_list = []
    for i, (name, price) in enumerate(items.items(), 1):
        item_list.append({name: price})
        print(f"{i:>4} | {name:<10} | {price:.2f}")
    item_list.append("Exit shop?")
    print("-" * 27)
    print(f"{len(item_list):>4} | Exit shop? \n")
    return item_list

# Validation functions


def validate_if_in_range(user_input, item_list):
    """Check if user's input is in list range"""
    user_input = int(user_input)
    if user_input not in range(1, len(item_list)+1):
        raise ValueError(f"We do not seem to have this item in stock.\
    Please select item between 1 and {len(item_list)-1} or 6 to exit.")


def validate_if_number(user_input):
    """Check if user's input is a number"""
    if user_input.isalpha() or user_input.isalnum() and not user_input.isdigit():
        raise ValueError("Invalid input. Your selection must be a number")


def validate_confirmation(user_input):
    """Check if y/n confirmation is valid and exit if n"""
    if user_input not in ['y', 'n']:
        raise ValueError("Invalid input. Please type in 'y' or 'n'.")
    if user_input == 'n':
        quit()


def validate_budget(budget, price):
    """Check if budget is higher than the price"""
    if budget < price:
        raise BudgetTooLow("You do not have enough money to buy this item.")


def validate_attempts(attempt):
    """Check numbe of attempts"""
    if attempt == 3:
        raise TooManyAttempts(
            "You many unsuccessful attempts. Try again later")


def make_selection(item_list):
    """Ask user to select the item"""
    while True:
        option = input("From the table above select the option you want. ")
        try:
            validate_if_number(option)
            validate_if_in_range(option, item_list)
        except ValueError as error:
            print(F"{error} Try again")
            continue
        else:
            option = int(option)
            selection = item_list[option-1]
        return selection


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
        # if price > customer_budget:
        while True:
            try:
                increase_budget = input(
                    "Do you want increase your budget? y/n ").lower()
                validate_confirmation(increase_budget)
                extra_budget = input(
                    "Please type by how much more you can spend: ")
                validate_if_number(extra_budget)
                attempt += 1
                customer_budget += int(extra_budget)
                print(f"You inreased your budget to £{customer_budget}")
                validate_attempts(attempt)
                validate_budget(customer_budget, price)
                print(
                    f"Congratulations on your purchase. Here’s your item: \
                    \n {item.upper()} - £{price}")
                break
            except ValueError as v_error:
                print(v_error)
            except TooManyAttempts as c_error:
                print(c_error)
                break

    else:
        print(
            f"Congratulations on your purchase. Here’s your item: \n {item.upper()} - £{price}")
    finally:
        print(thank_you_mssg)
        quit()


def run_shop():
    """Run shop program"""
    options = setup(stock)
    selection = make_selection(options)
    check_budget(selection)


if __name__ == '__main__':
    run_shop()
