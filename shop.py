
# 1.	Create a dictionary with a minimum of 3 items and prices
# a.	One of the items needs to cost more than £100
stock = {'charger': 11, 'kettle': 25, 'headphones': 75, 'stereo': 140, 'Robot': 99.50}

# 2.	Customer’s available money is £100
thank_you_mssg = "Thank you for visiting out shop! Goodbye."
customer_budget = 100

# Custom error
class TooManyAttempts(ValueError):
    """Raise when user tries to purches item more than 3 times."""
    pass

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
    return item_list

# 4.	Accept the option as an input, an invalid input should raise a ValueError

def validate_input(user_input, item_list):
    """Get user's selection"""
    if user_input.isalpha() or user_input.isalnum() and not user_input.isdigit():
        raise ValueError("Invalid input. Your selection must be a number")
    user_input = int(user_input)
    if user_input not in range(1,len(item_list)+1):
        raise ValueError("We do not seem to have this item in stock.")

    return user_input


# If the customer can afford it, print out a message saying “Here’s your {item}!” 
# 6.	The user should be then greeted out of the shop, and the program terminated.

# 7.	If the customer cannot afford it, note the attempt and ask if they have more money, if they do and enter the amount it should be added to the balance.
# 8.	The purchase should be tried a maximum of 3 items, if it fails a custom error should be raised and the customer will exit the shop.

def run_shop():
    """Run shop program"""
    options = welcome(stock)
    customer_budget = 100
    while True:
        option = input("From the table above select the option you want. ")
        try:
            validate_input(option, options)
        except ValueError as error:
            print(F"{error}. Try again")
            continue
        else:
            if option == len(options):
                print(thank_you_mssg)
                quit()
                
            selection = options[int(option)-1]
            for k, v in selection.items():
                item = k
                value = v
            if value <= customer_budget:
                print(f"Here’s your {item}")
                break
            else: 
                n = 1
                while n < 2:
                    
                    increase_budget = ""
                    while increase_budget not in ['y', 'n']:
                        increase_budget = input("You cannot afford this item. Can you increase your budget? y/n ").lower()
                    
                        continue
                    if increase_budget == 'n':
                        print(thank_you_mssg)
                        quit()
                    else:
                        extra_budget = input("Please type by how much more you can spend: ")
                        
                        customer_budget += int(extra_budget)
                        if value > customer_budget:
                            n += 1
                            print(f"Your budget is increased to £{customer_budget}, but it still not enough.")
                            continue
                        else: 
                            print(f"Here’s your {item}")
                            break
                raise TooManyAttempts("You tried too many times, try again later.")
                
        finally: # always run this code
            print(thank_you_mssg)

run_shop()
