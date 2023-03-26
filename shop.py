
# 1.	Create a dictionary with a minimum of 3 items and prices
# a.	One of the items needs to cost more than £100
stock = {'charger': 11, 'kettle': 25, 'headphones': 75, 'stereo': 140, 'Robot': 99.50}

# 2.	Customer’s available money is £100
customer_budget = 100

# 3.	Welcome the customer and display the items and their prices, along with an option to “exit” 
def welcome(items):
    """Print welcome and display times in the shop"""
    print("Welcome to the shop!")
    print("What we have currently in stock: \n")
    # print table headers
    print("Opt. |".rjust(4) + "Item".ljust(12) +"| Price")
    print("-" * 5 + "|" + "-" * 12 + "|"+ "-" * 8 )
    # go over items and add them to a list along with their option to use for user input
    item_list = []
    for i, (name, price) in enumerate(items.items(),1):
        item_list.append({name: price})
        print(f"{i:>4} | {name:<10} | {price:.2f}")
    item_list.append("Exit shop?" )
    print("-" * 27)
    print(f"{len(item_list):>4} | Exit shop? \n")
    # print(item_list)
    return item_list

# 4.	Accept the option as an input, an invalid input should raise a ValueError

def validate_input(user_input, item_list):
    """Get user's selection"""
    if user_input.isalpha() or user_input.isalnum() and not user_input.isdigit():
        raise ValueError("Invalid input. Your selection must be a number")
    user_input = int(user_input)
    if user_input not in range(1,len(item_list)+1):
        raise ValueError("We do not seem to have this item in stock. Try again.")
    
    return(user_input)


# If the customer can afford it, print out a message saying “Here’s your {item}!” 
# 6.	The user should be then greeted out of the shop, and the program terminated.

# 7.	If the customer cannot afford it, note the attempt and ask if they have more money, if they do and enter the amount it should be added to the balance.
# 8.	The purchase should be tried a maximum of 3 items, if it fails a custom error should be raised and the customer will exit the shop.

def run_shop():
    """Run shop program"""
    options = welcome(stock)
    option = input("From the table above select the option you want. ")
    try:
        validate_input(option, options)
        # check if selection is last option => exit and quit program
        if option == len(options):
            print("Thank you for visiting out shop! Goodbye.")
            quit()
        selection = options[int(option)-1]
        for v in selection.values():
            value = v
        if value > customer_budget:
            print("You don't have enough money.")
    except ValueError as error:
        print(error)
        # continue
    finally:
        pass

run_shop()	