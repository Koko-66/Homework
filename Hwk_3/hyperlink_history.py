"""A] Simulate clicking around the CFG Website. Keep track of the URL changes and print the current URL after each move.
You will need to display the options for each link, and include an option for ‘Back’ if not on the Base URL. 
You do not need to worry about error handling 
You are recommended to keep the simulation going within a while True loop so the logic keeps looping until an exit is forced. 
You only need to consider the following URLs for your solution:
Base URL: https://codefirstgirls.com/  
Category URLs: /courses ,/opportunities/  
Sub-category URLs: /courses/cfgdegree/ , /opportunities/ambassadors/ 


Space/time complexity analysis:
Assumptions: 
- the depth of the link is assumed to be maximum 3
- links dictonary assumed to be already set
- since only the last part of the url will be manipulated at any time (the user cannot select the middle or begining of the url) there is no need to implement deque

1. create_url(url): time complexity is O(n) since we are joining the elements in the list and the length of the operation will depend on the number of elements in the list, n. Space complexity here is O(1) since apart from the joined string we are not creating any new data structures.
2. get_options(url): since the function traverses a dictionary that has embedded nested list, it's time complexity will depend on the number of categories (n) as well as number of subcategories (m) therefore the time complexity for the function is O(n+m). Space complexity is O(1) since as above, the function only produces a joined string and does not produce any additional structures.
3. select_next(current_url): both space and time complexity of this function are O(1) - the function will always have only one input and 1 data structure
4. selection_valid(current_url, selection): since the function calls upon get_options which traverses categories (n) and subcategories (m), it will depend on the length of these and therefore have time of complexity - O(n+m). The complexity introduced with split will be the same as that of either number of categories or subcategories, so can be ignored in this example. Space complexity is O(1) since we only crete list of options and no additional structures are created.
5. click(current_url, selection): both space and time complexity of this function is O(1) - the function only accesses (either pops or appends) the lst element of the url without the need to traverse the list and does not create any additonal data structures
6. run(base_url): the time complexity of this function depends on the number of times the user decides to perform operations. Other than that, it inherits the complexity from the functions incorporated in the loop. Space complexity of the function will increase with the lenght of the url, which in this case will be n(3) (considering the assumption of the max url depth).

Summing up:
The worse case scenario of time complexity is casued by traversing the categories dictionary, with complexity of O(n+m) and the space can be considered as O(1)
"""


# setup
base_url = "https://codefirstgirls.com"

# Dictonary structure for the urls to allow expansion
# categories_dict = {category1:[subcategory1, subcategory2], category2: [subcategory1, subcategory2] }
categories_dict = {"Courses":["CFGDegree"], "Opportunities":["Ambassadors"]}
# max link depth assumed in the tasks
max_depth = 3


def create_url(url):
    """
    Returns a string of the current url
    input: url (list)
    output: url (string
    """
    return '/'.join(url)


def get_options(url):
    """
    Returns a string of the options
    input: url (list)
    output: options (string)
    """

    # check if url is base and set categories as options
    if url[-1] == base_url:
        options = []
        for cat in categories_dict:
            options.append(cat)
        return ' '.join(options)
    
    # if url is not base load subcategories
    elif len(url) == 2:
        for cat, subcat in categories_dict.items():
            if url[-1] == cat.lower():
                return ' '.join(subcat + ["Back"])
    else:
        return "Back"


def select_next(current_url):
    """
    Returns a string of the selection
    input: current_url (list)
    output: selection (string)
    """

    selection = input(f"Options: {get_options(current_url)}\n")
    return selection.lower()


def selection_valid(current_url, selection):
    """Check if user selection is valid"""
    
    available_options = [option.lower() for option in get_options(current_url).split()]

    if selection in available_options:
        return True


def click(current_url, selection):
    """
    Returns a the new url after clicking
    input: current_url (list), selection (string)
    output: current_url (list)
    """
    # going back
    if selection == "back":
        # check if user is already at base url
        if len(current_url) == 1:
            print("\n!!!")
            print("This is the base url, you cannot go back")
        else: current_url.pop()
        
    else:
        # check if the current url reached max length
        if len(current_url) == max_depth:
            print("\n!!!")
            print("No further links available. You can only go back.")
        else:
            
            # check if the selection is valid i.e. appears in available options
            if selection_valid(current_url, selection):
                current_url.append(selection)
            else:
                print("\n!!!")
                print("Invalid selection")
                
    return current_url


def run(base_url):
    """
    Runs the program
    input: base_url (string)   
    """
    current_url = [base_url]
    while True:
        print("-" * 50+"\n")
        print(f"You are currently here: {create_url(current_url)}")
        print("." * 50+"\n")
        print("Where would you like to go next?\n")
        selection = select_next(current_url)
        click(current_url, selection)


if __name__ == "__main__":
    run(base_url)
