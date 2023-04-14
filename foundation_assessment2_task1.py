import collections
"""Write a function that takes in an input and checks to see if it’s an isogram. The function should return True or False."""

def check_if_isogram(word):
    # find out counts for all letters in the word
    word_counts = collections.Counter(word)
    # if the max count is greater than 1, then it's not an isogram
    if max(word_counts.values()) > 1:
        return False
    return True

print(check_if_isogram("isogram"))
print(check_if_isogram("uncopyrightable"))
print(check_if_isogram("ambidextrously"))
print(check_if_isogram("where"))


