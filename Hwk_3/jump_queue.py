"""
Time/space complexity analysis:
For loop has time complexity of O(n) because it the time it will run will increase proportionally to the length of lines in the input file
The deque methods for creating a deque object and appedning items to the start and the end of the queue all have time complexity of O(1) since they do not require traversing the queue
The whole function has a space complexity of O(n) because the space needed to store the final queue will increase proportionally to the length of the input
Therefore, the time/space complexity of the whole function is O(n), since this is the worst case scenario which will have the most impact on the performance of the program.
"""

from collections import deque

def jump_queue(filename):
    """Takes in a file with a list of names and whether they are joining or jumping the queue and returns a list of names in the order they are in the queue."""
     # create deque object
    queue = deque() 
    # open the file
    with open(filename) as file:
        for line in file: 
            # strip spaces and split into JUMP/JOIN and name
            line = line.strip().split()
            # add to the end of the queue
            if line[0] == "JOIN":
                queue.append(line[1])
            # add to the start of the queue
            elif line[0] == "JUMP":
                queue.appendleft(line[1])
    return list(queue)

print(jump_queue("HWK_3/hw3_q1.txt"))
 