"""Task 2: Write a function that returns the Nth number in the following sequence
8, 15, 22, 29, 36, …
For example:
●	num_in_seq(1)  = 8
●	num_in_seq(5) = 36
●	num_in_seq(10) = 71
"""

# Method 1
def num_in_seq(n):
    """
    Returns the Nth number in the sequence 
    8, 15, 22, 29, 36, … - divide and conquer
    """

    if n == 1: # base case
        return 8
    # for others return previous number increased by 7
    return num_in_seq(n-1)+7
    

# Method 2
cache = {1: 8}

def num_in_seq2(n):
    """As above  with memoization"""

    if n in cache: # base case (set in cache)
        return cache[n]

    cache[n] = num_in_seq2(n-1)+7
    return cache[n]


print("-"*10,"divide and conquer","-"*10)
print(num_in_seq(1))
print(num_in_seq(5))
print(num_in_seq(10))
# print(num_in_seq(1000)) # this thows "Maximum recursion depth exceeded"

print("-"*10,"dynamic - with memoization","-"*10)
print(num_in_seq2(1))
print(num_in_seq2(5))
print(num_in_seq2(10))
print(num_in_seq2(1000))

