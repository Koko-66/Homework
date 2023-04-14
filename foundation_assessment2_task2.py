"""You are tasked with calculating the minimum classes we need to have so we know how many people to employ. Write a function which when given a number of students, calculates and prints out a string for your proposed number of classes, and a dictionary showing the allocation. 
Key Constraints:
●	The maximum size of a class is 30
●	There needs to be a minimum of 2 classes
●	The distribution of each class should be as even as possible. 
●	We want to hire as little people as possible - so where possible focus on bigger classes, and less of them!
Inputs/Outputs:
●	If 31 was the input, the output would be:
Proposed Allocation: 2 classes
{'Class 1': 16, 'Class 2': 15}
●	If 59 was the input, the output would be:
Proposed Allocation: 2 classes
{'Class 1': 30, 'Class 2': 29}
●	If 87 was the input, the output would be:
Proposed Allocation: 3 classes
{'Class 1': 29, 'Class 2': 29, 'Class 3': 29}
"""



def get_classes(students_no):
    # create a dictionary to store the allocation
    allocation = {}

    #  base case when we have fewer than 30 students
    if students_no <= 30:
        no_classes = 2
        allocation = {"Class 1": students_no - students_no // 2, "Class 2": students_no // 2}

    # if students number is higher, divide by 30 usign floor division to check how many classes we need and then find the remainder of students that are left over
    else: 
        no_classes = students_no // 30
        if students_no % 30 > 0:
            no_classes += 1
       
    students_per_class = students_no // no_classes     
    remainder = students_no % no_classes
    # loop through the number of classes and allocate students to each 
    for i in range(no_classes):
        # if the remainder is greater than 0, add 1 to the number of students in each class
        if remainder > 0:
             allocation[f"Class "] = students_per_class+1
        # else:
            

    print(f"Proposed Allocation: {no_classes} classess \n{allocation}")

get_classes(15)
get_classes(31)
get_classes(59)
get_classes(87)



